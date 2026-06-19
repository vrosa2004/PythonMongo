from pymongo import MongoClient

connection_string = "mongodb://admin:secretpassword@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["meuBanco"]

print(db_connection)
print()
collection = db_connection.get_collection("minhaCollection")

print(collection)
print()

search_filter = { "estou": "aqui" }

response = collection.find(search_filter)
print(response)

for registry in response: print(registry)

collection.insert_one({
    "estou": "inserindo",
    "numero": [123, 456, 789]
})