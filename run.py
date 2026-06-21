from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

minha_collection_repository = MinhaCollectionRepository(db_connection)

order = {
    "name": "Vinicius",
    "endereco": "Rua 123",
    "pedidos": {
        "pizza": 1,
        "hamburguer": 5,
        "pizza_doce": 1
    },
    "cpf": 123456
}

minha_collection_repository.insert_document(order)

list_of_documents = [
    {"eric": "cartman"},
    {"stan": "march"},
    {"kenny": "mcCormick"},
    {"kyle": "broflovski"}
]

minha_collection_repository.insert_list_of_documents(list_of_documents)