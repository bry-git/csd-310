from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ahowo.mongodb.net/admin?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech


def get_all_students():
    docs = db.students.find({})
    print(f"\n -- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")
    for doc in docs:
        print(f"Student ID: {doc['student_id']}")
        print(f"First Name: {doc['first_name']}")
        print(f"Last Name: {doc['last_name']} \n")
    input("end of program, press any key to continue")


def update_student(target_id, update_key, update_value):
    print("DEBUG " + update_key + " " + update_value)
    result = db.students.update_one({"student_id": target_id}, {"$set": {f"{update_key}": f"{update_value}"}})
    print(f"-- DISPLAYING STUDENT DOCUMENT FOR {target_id}")
    print(result)
    print(f"Student ID: {result['student_id']}")
    print(f"First Name: {result['first_name']}")
    print(f"Last Name: {result['last_name']} \n")
    input("end of program, press any key to continue")


def get_student_by_id(student_id):
    doc = db.students.find_one({"student_id": student_id})
    print(f"\n -- DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY --")
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']} \n")
    input("end of program, press any key to continue")


get_all_students()
update_student(1007, "last_name", "frankfurter")
get_student_by_id(1007)
