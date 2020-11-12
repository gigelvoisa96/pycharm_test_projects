# import connection requests library
from mongoDATA import MongoClient

# Create a new connection to a single MongoDB instance at host:port.
connection = MongoClient()

# Create and get a data base (db) from this connection
db = connection.test

# Create and get a collection named "collect" from the data base named "db" from the connection named "connection"
collection = db.collect

# Create an entry and insert in the collection
age = 30
entry = {"Name": "Ralph",
         "Address": "16, Av Foch",
         "Age in Years": age}
collection.insert(entry)

# Print out the inserted entry
print(list(collection.find()))

# close connection
connection.close()
