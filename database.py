from pymongo import MongoClient

uri = "mongodb://localhost:27017/product_inventory"
client = MongoClient(uri)

def get_database():
    try:
        print("Connected to MongoDB successfully!")
        return client['product_inventory']
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
