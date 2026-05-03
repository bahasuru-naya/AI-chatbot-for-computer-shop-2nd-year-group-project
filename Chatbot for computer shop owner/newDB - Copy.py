from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace <db_password> with the actual password
uri = "mongodb+srv://gpsd:helloworld@gpsd0.3fvcw.mongodb.net/?retryWrites=true&w=majority&appName=gpsd0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



field_names = [
    "_id",
    "$oid",
    "id",
    "$numberInt",
    "item_name",
    "Item_Pic_Url",
    "Item_detail",
    "stock",
    "price",
    "$numberDouble",
    "warranty_in_months",
    "sales",
    "SaleID",
    "QuantitySold",
    "SaleDate"
]
