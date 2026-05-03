from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Replace with your actual MongoDB connection string
uri = "mongodb+srv://gpsd:helloworld@gpsd0.3fvcw.mongodb.net/?retryWrites=true&w=majority&appName=gpsd0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the ComputerStore database
db = client['ComputerStore']

# Source collections
items_col = db['items']
stock_col = db['stock']
price_col = db['price']
warranty_col = db['warranty']
sales_col = db['sales']

# New merged collection
merged_col = db['merged_collection']

# Clear the merged collection if it already exists
merged_col.delete_many({})

# Iterate over each item in the items collection
for item in items_col.find():
    item_id = item['id']
    
    # Find the corresponding stock document
    stock_doc = stock_col.find_one({'id': item_id})
    item['stock'] = stock_doc['stock'] if stock_doc else None
    
    # Find the corresponding price document
    price_doc = price_col.find_one({'id': item_id})
    item['price'] = price_doc['price'] if price_doc else None
    
    # Find the corresponding warranty document
    warranty_doc = warranty_col.find_one({'id': item_id})
    item['warranty_in_months'] = warranty_doc['warranty_in_months'] if warranty_doc else None
    
    # Find all corresponding sales documents
    sales_docs = list(sales_col.find({'id': item_id}, {'_id': 0}))
    item['sales'] = sales_docs if sales_docs else []
    
    # Insert the merged document into the new collection
    merged_col.insert_one(item)

print("Data merged successfully!")
