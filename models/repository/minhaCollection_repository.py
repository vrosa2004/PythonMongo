from bson.objectid import ObjectId
from typing import Dict, List

class MinhaCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "minhaCollection"
        self.__db_connection = db_connection

    def insert_document (self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            filter,
            { "endereco": 0, "_id": 0 }
        )

        response = []
        for elem in data: response.append(elem)

        return response

    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, {"_id": 0})
        return response

    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "cpf": {"$exists": True } })
        for x in data: print(x)

    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            { "name": "Vinicius" },
            {"endereco": 0, "_id": 0}
        ).sort([("pedidos.pizza", 1)])

        for elem in data: print(elem)

    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "$or": [{ "name": "Vinicius" }, {"eric": { "$exists": True } }] })
        for x in data: print(x)
        print()

    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"_id": ObjectId("6a3774aee918f8aa138b4860") })
        for x in data: print(x)

    def edit(self, name):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one(
            {"_id": ObjectId("6a3774aee918f8aa138b4860") },
            { "$set": { "name": name } }
        )
        print(data.modified_count)

    def edit_many(self, filtro, propriedades):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            filtro,
            { "$set": propriedades },
        )
        print(data.modified_count)

    def edit_many_increment(self, num):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            {"_id": ObjectId("6a3774aee918f8aa138b4860")},
            {"$inc": { "idade": num }}
        )
        print(data.modified_count)

    def delete(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one( {"_id": ObjectId("6a3774aee918f8aa138b4860") })
        print(data.deleted_count)

    def delete_many(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many( {"_id": ObjectId("6a3774aee918f8aa138b4860") })
        print(data.deleted_count)