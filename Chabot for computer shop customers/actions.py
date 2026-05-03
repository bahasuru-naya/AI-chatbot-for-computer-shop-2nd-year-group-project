from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from groq import Groq


def create_sql_connection():
    username = 'root'
    password = 'bahasurubn0008'
    host = 'localhost'
    port = 3306
    database = 'ComputerStore'
    # Construct the connection URL
    connection_url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"

    # Create the SQLAlchemy engine
    engine = create_engine(connection_url)

    # Create and return the connection
    connection = engine.connect()
    return connection


client = Groq(
    api_key="",
)


class ActionFindComponents(Action):
    def name(self) -> Text:
        return "action_find_components"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])

        if entities:
            application_name = entities[0]['value']

            connection = create_sql_connection()

            # Query the database
            query = f"SELECT * FROM Appspec WHERE App_Name = '{application_name}'"
            result = connection.execute(query).fetchone()

            # Close the database connection
            connection.close()

            if result:
                components = {
                    'application_type': result['App_Type'],
                    'processor': result['Processor'],
                    'storage': result['Storage'],
                    'video_ram': result['Video_RAM'],
                    'ram': result['RAM']
                }

                response_message = domain["responses"]["utter_components"][0]["text"].format(
                    application_name=application_name,
                    application_type=components['application_type'],
                    processor=components['processor'],
                    storage=components['storage'],
                    video_ram=components['video_ram'],
                    ram=components['ram']
                )

                dispatcher.utter_message(response_message)
            else:
                dispatcher.utter_message(text="I couldn't find any components for that application. Please try again "
                                              "or provide more details.")
        else:
            dispatcher.utter_message(
                text="You haven't provided the application name. Please specify the application name \n"
                     "for component recommendations.")

        return []


class ActionGivePrice(Action):
    def name(self) -> Text:
        return "action_give_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])

        if entities:
            item_name = entities[0]['value']

            connection = create_sql_connection()

            # Query the database for price and stock
            query = f"""
            SELECT  p.price, s.stock
            FROM stock s
            JOIN price p ON s.id = p.id
            JOIN items i ON s.id = i.id
            WHERE i.item_name = '{item_name}';
            """
            result = connection.execute(query).fetchone()

            # Close the database connection
            connection.close()

            if result:
                price, stock = result

                if stock > 0:
                    dispatcher.utter_message(
                        f"{item_name} price is: Rs {price:.2f} and It is available. You can buy it from us."
                    )
                else:
                    dispatcher.utter_message(f"{item_name} price is: Rs {price:.2f} and It is currently out of stock. "
                                             f"You can check it later.")
            else:
                dispatcher.utter_message("Sorry, I couldn't find that item in our store.")
        else:
            dispatcher.utter_message("You haven't provided the item name. Please specify the item name.")

        return []


class ActionShowItem(Action):
    def name(self) -> Text:
        return "action_show_item"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])

        if entities:
            item_name = entities[0]['value']

            connection = create_sql_connection()

            # Query the database

            query = f"""
                        SELECT items.Item_Pic_Url 
                        FROM items                        
                        WHERE items.item_name = '{item_name}'                        
                        """
            result = connection.execute(query).fetchone()

            # Close the database connection
            connection.close()

            if result:
                components = {
                    'url': result['Item_Pic_Url']

                }

                dispatcher.utter_message(
                    text=f"Here is an image of {item_name}\n",
                    image=components['url']
                )

            else:
                dispatcher.utter_message("Sorry, I couldn't find that item in our store.")
        else:
            dispatcher.utter_message("You haven't provided the item name. Please specify the item name")

        return []


class ActionListAvailableItems(Action):
    def name(self) -> Text:
        return "action_list_available_items"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Create SQL connection
        connection = create_sql_connection()

        # Query the database for available items
        query = """
        SELECT i.item_name, p.price 
        FROM items i
        JOIN price p ON i.id = p.id
        JOIN stock s ON s.id = p.id
        WHERE s.stock > 0
        """
        results = connection.execute(query).fetchall()

        # Close the database connection
        connection.close()

        if results:
            available = "Here are the available items with price in our store:"
            for item_name, price in results:
                available = available + "\n" + f"- {item_name}: Rs {price:.2f}"

            dispatcher.utter_message(available)
        else:
            dispatcher.utter_message("Sorry, there are no available items in our store at the moment.")

        return []


class ActionCheckItemAvailability(Action):
    def name(self) -> Text:
        return "action_check_item_availability"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])

        if entities:
            item_name = entities[0]['value']

            connection = create_sql_connection()

            # Query the database for stock of the specified item
            query = f"""
            SELECT s.stock, p.price
            FROM stock s
            JOIN price p ON s.id = p.id
            JOIN items i ON s.id = i.id
            WHERE i.item_name = '{item_name}'
            """
            result = connection.execute(query).fetchone()

            # Close the database connection
            connection.close()

            if result:
                stock, price = result

                if stock > 0:
                    dispatcher.utter_message(
                        f"Yes, we have {stock} units of {item_name} in stock, priced at Rs {price:.2f}. You can buy "
                        f"it from us."
                    )
                else:
                    dispatcher.utter_message(
                        f"Sorry, {item_name} is currently out of stock. Please check back later."
                    )
            else:
                dispatcher.utter_message("Sorry, I couldn't find that item in our store.")
        else:
            dispatcher.utter_message("You haven't provided the item name. Please specify the item name.")

        return []


class ActionCheckDiscount(Action):
    def name(self) -> Text:
        return "action_check_discount"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        if entities:
            item_name = entities[0]['value']

            connection = create_sql_connection()

            query = f"""
            SELECT i.item_name, p.price, d.discount_rate
            FROM items i
            JOIN price p ON i.id = p.id
            JOIN discount d ON i.id = d.id
            WHERE i.item_name = '{item_name}'
            """

            result = connection.execute(query).fetchone()

            # Close the database connection
            connection.close()

            if result:
                item_name, discounted_price, discount_rate = result
                original_price = discounted_price * (100 / (100 - discount_rate))
                dispatcher.utter_message(text=f"The original price of {item_name} is Rs.{original_price:.2f}. \n"
                                              f"With the discount, the price is Rs.{discounted_price:.2f}."
                                              f"The discount rate is {discount_rate}%.")
            else:
                dispatcher.utter_message(text=f"Sorry, no discount information available for {item_name}.")
        else:
            dispatcher.utter_message("You haven't provided the item name. Please specify the item name.")
        return []


class ActionCheckWarranty(Action):
    def name(self) -> Text:
        return "action_check_warranty"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        if entities:
            item_name = entities[0]['value']

            connection = create_sql_connection()
            query = f"""
            SELECT i.item_name, w.warranty_in_months
            FROM items i
            JOIN warranty w ON i.id = w.id
            WHERE i.item_name = '{item_name}'
            """
            result = connection.execute(query).fetchone()

            # Close the database connection
            connection.close()

            if result:
                item_name, warranty_months = result
                dispatcher.utter_message(text=f"The warranty for {item_name} is {warranty_months} months.")
            else:
                dispatcher.utter_message(text=f"Sorry, warranty information is not available for {item_name}.")
        else:
            dispatcher.utter_message("You haven't provided the item name. Please specify the item name.")
        return []


class ActionDescribeItem(Action):
    def name(self) -> Text:
        return "action_describe_item"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        if entities:
            item_name = entities[0]['value']
            engine = create_sql_connection()
            Session = sessionmaker(bind=engine)
            session = Session()

            query = f"SELECT item_detail FROM items WHERE item_name = :item_name"
            result = session.execute(query, {'item_name': item_name}).fetchone()

            # Close the session
            session.close()

            if result:
                item_detail = result[0]
                dispatcher.utter_message(text=f" {item_detail}")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't find any details for the item '{item_name}'.")
        else:
            dispatcher.utter_message(text="You haven't provided the item name. Please specify the item name.")
        return []


class ActionNLUFallback(Action):
    def name(self) -> Text:
        return "action_nlu_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the latest user message
        user_message = tracker.latest_message['text']
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": f"{user_message} answer this question without greetings in one paragraph as computer "
                               f"shop customer assistant in RK Computers and CCTV Operations at sri lanka and also "
                               f"write answer briefly and Don't answer unrelated questions about computer shop and "
                               f"explain customer you can only answer computer shop related questions "


                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        final_output = ""
        for chunk in completion:
            # print(chunk.choices[0].delta.content or "", end="")
            final_output += chunk.choices[0].delta.content or ""
        print(final_output)
        # remove unnecessary spaces
        cleaned_text = ' '.join(final_output.split())
        # Custom logic using user_message
        dispatcher.utter_message(text=f"{cleaned_text}")

        return []
