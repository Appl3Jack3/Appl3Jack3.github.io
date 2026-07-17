# Example Python Code to Insert a Document 

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for the Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        self.client = MongoClient(
            f"mongodb://{USER}:{PASS}@localhost:27017/?authSource=AAC"
    )
        # Select database and collection
        self.database = self.client["AAC"]
        self.collection = self.database["aac_shelter_outcomes.csv"]

    def create(self, data):
        """Insert a new document into the collection."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return True if result.inserted_id else False
            except Exception as e:
                print(f"Create Error: {e}")
                return False
        return False

    def read(self, query=None):
        """Read documents from the collection."""
        try:
            if query:
                return list(self.collection.find(query))
            else:
                return list(self.collection.find())
        except Exception as e:
            print(f"Read Error: {e}")
            return []

    def update(self, query, updates):
        """Update document(s) matching the query."""
        if query and updates:
            try:
                result = self.collection.update_many(query, {"$set": updates})
                return result.modified_count
            except Exception as e:
                print(f"Update Error: {e}")
                return 0
        return 0

    def delete(self, query):
        """Delete document(s) matching the query."""
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Delete Error: {e}")
                return 0
        return 0
