from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ahowo.mongodb.net/admin?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

data = [{
    "student_id": 1007,
    "first_name": "thorin",
    "last_name": "oakensheild"
},
    {
    "student_id": 1008,
    "first_name": "bilbo",
    "last_name": "baggins"
},
    {
    "student_id": 1009,
    "first_name": "frodo",
    "last_name": "baggins"
}]


def seed_data(data):
    print("\n -- INSERT STATEMENTS --")
    for doc in data:
        inserted_id = db.students.insert_one(doc).inserted_id
        print(f"Inserted student record {doc['first_name']} {doc['last_name']} into the students collection with document_id: {inserted_id}")

seed_data(data)