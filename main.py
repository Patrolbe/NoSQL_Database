import pprint
import uuid
from magic_store.kv_idea.store import Store
from magic_store.db.database import Database

def test():
    store = Store()
    result = store.put("key1", "test text")
    result = store.put("key1", "test text 2", namespace="osiolek")
    result = store.put("key1", "nierozwazna czynnosc")

    x = store.get("key1", namespace="osiolek")
    print(x)
    result = store.delete("key1", namespace="osiolek", guard=x["guard"])
    result = store.put("key1","def", namespace="osiolek")
    # result = store.put("key1", "xxxxxxxxxxxxxxx", guard=x["guard"])

    print(result)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(store._store)

    result = store.save()
    print(result)


def testLoad():
    store = Store()
    result = store.load()
    print(result)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(store._store)

if __name__ == '__main__':

    database = Database()

    user = {
        "imie": "Patryk1",
        "nazwisko": "Blizniewski1",
        "login": "Patrol1"
    }
    database.createUser(user, "id1")
    database.searchUser("id1")
    userUpdate = {
        "imie": "Patryk",
        "nazwisko": "Blizniewski",
        "login": "Patrol",
    }
    database.updateUser("id1", userUpdate)
    file1 = {
        "file": "Zajecia1.xlsx",
        "path": "D:\\Studia 5 semestr\\Metody numeryczne\\Cwiczenia\\1 Zajecia\\Zajecia1.xlsx",
    }
    file2 = {
        "file": "2 Zajecia.xlsx",
        "path": "D:\\Studia 5 semestr\\Metody numeryczne\\Cwiczenia\\2 Zajecia.xlsx",
    }
    file3 = {
        "file": "6 Zajecia.xlsx",
        "path": "D:\\Studia 5 semestr\\Metody numeryczne\\Cwiczenia\\6 Zajecia.xlsx",
    }

    database.createFile("id1", ["Mn", "Lek1"], file1)
    database.createFile("id1", ["Mn", "Lek2"], file2)
    database.createFile("id1", ["Mn", "Lek6"], file3)
    database.createFile("ebebe", ["Lek7"], file3)
    #database.deleteUser("id1")

    database.searchFileByTags("id1", ["Mn", "Lek1"], 2)
    database.searchFileByTags("id1", ["Mn", "ebebe"], 2)

    #database.deleteTag("id1", "Mn")
    #database.deleteFileFromTag("id1", "Mn", "2 Zajecia.xlsx")
    #database.deleteFileFromAllTags("id1", "2 Zajecia.xlsx")

