from pymongo import MongoClient


def test_mongodb_connection():
    try:
        # Replace 'mongodb://localhost:27017/' with your MongoDB connection string if different
        client = MongoClient("mongodb://localhost:27017/")
        # Attempt to list databases to verify connection
        databases = client.list_database_names()
        print("MongoDB connection successful. Databases:", databases)
    except Exception as e:
        print("Failed to connect to MongoDB:", e)


if __name__ == "__main__":
    test_mongodb_connection()
