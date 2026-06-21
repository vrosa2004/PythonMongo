from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

minha_collection_repository = MinhaCollectionRepository(db_connection)

# filtro = { "endereco": "Rua 123" }
#
# minha_collection_repository.edit_many(filtro, { "idade": 22 })

# minha_collection_repository.edit_many_increment(-3)

#minha_collection_repository.delete()

minha_collection_repository.delete_many()