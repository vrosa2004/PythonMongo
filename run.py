from models.connection_options.connection import DBConnectionHandler

db_handle = DBConnectionHandler()
conn1 = db_handle.get_db_connection()
print(conn1)
print()

db_handle.connect_to_db()
conn2 = db_handle.get_db_connection()
print(conn2)
print()

collection = conn2.get_collection("minhaCollection")
print(collection)
print()

collection.insert_one({
    "estou": "inserindo",
    "numero": [123, 456, 789]
})

filter = collection.find({"estou": "inserindo"})

for repository in filter:
    print(repository)