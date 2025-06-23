from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username = 'accuser', password = 'Zelda5Persona5RoyalofTime',
        host = 'nv-desktop-services.apporto.com', port = 31714, db = 'AAC', col = 'animals'):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac databases, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environmnet.
        # 
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'accuser'
        #PASS = 'Zelda5Persona5RoyalofTime'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 31714
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[col]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is None:
            raise ValueError("Nothing to save, because data parameter is empty")
        if not isinstance(data, dict):
            raise TypeError("Data must be in a dictionary") #Check that the input is a dictionary to avoid runtime errors
        try:
            result = self.database.animals.insert_one(data) #data should be dictionary
            return result.inserted_id
        except Exception as e:
            raise Exception(f"Failed to insert data: {e}")
            return False

# Create method to implement the R in CRUD
    def read(self, filter_query=None):
        try:   
            if filter_query is None:
                filter_query = {} #Creates a new empty query to return all documents
            results = self.collection.find(filter_query) #Runs a MongoDB query against the 'animals' collection
            return list(results)
        except Exception as e:
            raise Exception(f"Failed to read data: {e}") #Raise exception if data is invalid

# Create method to implement U in CRUD
    def update(self, filter_query=None, new_data=None):
        try:
            if not filter_query:
                raise ValueError("No filter is provided for dictionary") #Raise exception if there is no filter provided
            if not new_data:
                raise ValueError("No data to update") #Raise exception if there is no updated data provided
            
            results = self.database.animals.update_many(filter_query, {"$set" : new_data}) #Data should be filter and dictionary
            return results.modified_count
        except Exception as e: 
            raise Exception(f"Failed to update: {e}") 

# Create method to implement D in CRUD
    def delete(self, filter_query=None):
        try:
            if not filter_query: 
                raise ValueError("No filter is provided for dictionary") #Raise exception if there is no filter provided
            results = self.database.animals.delete_many({})
            return results.deleted_count
        except Exception as e: 
            raise Exception(f"Failed to delete data: {e}") 
