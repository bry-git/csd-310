from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ahowo.mongodb.net/admin?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech


def get_all_docs(collection):
    docs = db.collection.find({})
    print(f"\n -- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")
    for doc in docs:
        print(f"Student ID: {doc['student_id']}")
        print(f"First Name: {doc['first_name']}")
        print(f"Last Name: {doc['last_name']} \n")
    input("end of program, press any key to continue")


def get_one_doc(collection, id):
    doc = db.collection.find_one(id)
    print(f"\n -- DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY --")
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']} \n")
    input("end of program, press any key to continue")

get_all_docs("students")
get_one_doc("students", {"student_id": "1007"})
