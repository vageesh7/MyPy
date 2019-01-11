# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient

class myMongoDB():

    def __init__(self):
        # workbook = xlrd.open_workbook("..\TestData\Test.xlsx")
        # self.worksheetName = workbook.sheet_by_name("Data")
        encoding = "utf-8"

    def connect_To_DB(self):
        print("Connect to DB Started")

        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            raise  Exception("Could not connect to MongoDB")
        db = conn.database
        return db

    def employeTable(self):
        db = self.connect_To_DB()
        collection = db.user_collection
        while True:
            # Program to create/Delete/Display a record in MongoDB
            Menu = int(input("""
            1. Create a Record 
            2. Delete a Record
            3. Display all The Records
            4. Exit the Connection

            Please Choose the Option ---->
            """))
            if Menu == 1:
                print("please enter the name ,address and phone number in order")
                empName = str(input("Enter the Name of the Employee:"))
                if (collection.find({'name': empName}).count() > 0):
                    print("Record already exist")
                    print(collection.find_one({"name": empName}))
                    yesOrNo = str(input("Do you want this record to be modified? y/n"))
                    if yesOrNo == 'y':
                        print("Enter the value to be updated, If not required Please press 'Enter' to skip the update")
                        addressUpdate = input("Address:")
                        phoneNumberUpdate = input("Phone Number, If more than one then separate by a Space:")
                        if (addressUpdate != ""):
                            db.user_collection.update_one({"name": empName},{"$set": {"address": addressUpdate,}})
                        elif(phoneNumberUpdate != ""):
                            db.user_collection.update_one({"name": empName}, {"$set": {"phone": [int(x) for x in phoneNumberUpdate.split()]}})
                        else:
                            print()

                    else:
                        print()

                else:
                   db.user_collection.insert_one(
                        {"name": empName, "address": input("Address:"),
                         "phone": [int(x) for x in
                                   input("Phone Number, If more than one then separate by a Space").split()]
                         }
                    )
                print("Inserted/Updated successfully.")
            elif Menu == 2:
                empName = str(input("Enter the Name of the Employee:"))
                if (collection.find({'name': empName}).count() > 0):
                    print("enter the name to delete the details")
                    db.user_collection.delete_one(
                        {"name": empName}
                    )
                else:
                    print(" !!! There is no Such a Record to Delete !!!")
            elif Menu == 3:
                for user_collection in collection.find():
                    print(user_collection)

            else:
                exit()


obj = myMongoDB()
obj.employeTable()
