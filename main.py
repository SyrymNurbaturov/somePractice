# Task 1
import time # is for realization method sleep
from pathlib import Path # for check is file exist in directory or not
import json # json file
import datetime # date object

print("Task 1")
done = False
while done == False:
    print("1. Create json file form ")
    print("0. Exit")
    option = int(input("Choose option: "))

    if option == 1: # conditions
        form_json_path = Path("form.json")# Path class (file path)
        if form_json_path.is_file(): # method for checking is file exist
            form_dict = dict(json.load(open("form.json")))
            form_dict_keys = list(form_dict.keys())
            fname = str(input("Please input your first name: "))
            lname = str(input("Please input your last name: "))
            mail = str(input("Please input your mail: "))
            number = int(input("Please input your phone number: "))
            access = True
            for i in form_dict.keys():# each keys
                if form_dict[i]["number"] == number: # for each keys check number
                    print("We have such number in file")
                    access = False

            if access: # if not such number
                birth_day = str(input("Please input your birthday (example: 19 December, 2002): "))
                birth_day_object = datetime.datetime.strptime(birth_day, "%d %B, %Y")
                birth_day_object = str(birth_day_object)
                form_dict[int(form_dict_keys[len(form_dict_keys)-1])+1] = {"fname":fname, "lname": lname, "mail": mail, "number":number,"birth_day":birth_day_object}

                with open("form.json", 'w') as form_jsonWF:
                    json.dump(form_dict, form_jsonWF, indent=2)

        else:
            print("There are no such file we try to create please wait: ")
            time.sleep(1) # there we sleep for 1 sec
            form = dict({})
            with open("form.json", 'w') as form_jsonWF: # creating empty dict to insert json file
                json.dump(form, form_jsonWF, indent=2)
            print("We created file")
            if 1==1:
                fname = str(input("Please input your first name: "))
                lname = str(input("Please input your last name: "))
                mail = str(input("Please input your mail: "))
                number = int(input("Please input your phone number: "))
                birth_day = str(input("Please input your birthday (example: 19 December, 2002): ")) # example we should enter in such position cause it will give us error
                birth_day_object = datetime.datetime.strptime(birth_day, "%d %B, %Y") # date object
                birth_day_object = str(birth_day_object)
                form[1] = {"fname":fname, "lname": lname, "mail": mail, "number":number, "birth_day":birth_day_object}

                with open("form.json", 'w') as form_jsonWF:
                    json.dump(form, form_jsonWF, indent=2)


    else:
        done = True

print("Task 2")

import sqlite3 as sql # instead of write sqlite3 i save it like sql and i can use methods like sqlite3.connect() as sql.connect()

done = False


while done==False:
    print("1. Create sqlite3 db form")
    print("0. Exit")
    option = int(input("Choose option: "))

    if option==1:
        form_json_path = Path("form.db")

        if form_json_path.is_file():
            conn = sql.connect('form.db')

            conn.execute('''CREATE TABLE IF NOT EXISTS FORM
                                (fname CHAR(50),
                                lname CHAR(50),
                                mail CHAR(50),
                                number integer,
                                birth_day CHAR(60));''') # creating table form

            cursor = conn.cursor() # cursor for manipulate with table
            fname = str(input("Please input your first name: "))
            lname = str(input("Please input your last name: "))
            mail = str(input("Please input your mail: "))
            number = int(input("Please input your phone number: "))
            cursor.execute("SELECT 1 FROM form WHERE number = %s" % (number)) # we check if in db we have such number
            data = cursor.fetchall() # if we have the data save that
            if len(data)==0: # if len == 0 it means no such number
                birth_day = str(input("Please input your birthday (example: 19 December, 2002): "))
                birth_day_object = datetime.datetime.strptime(birth_day, "%d %B, %Y")
                birth_day_object = str(birth_day_object)
                cursor.execute("INSERT INTO FORM (fname, lname, mail, number, birth_day) VALUES ('%s', '%s', '%s',%s,'%s')" % (fname, lname, mail, number, birth_day_object))
                conn.commit()# save in db
            else:
                print("We have such number in db")


        else:
            print("There are no such db we try to create please wait: ")
            time.sleep(1)
            conn = sql.connect('form.db')

            conn.execute('''CREATE TABLE IF NOT EXISTS FORM
                                (fname CHAR(50),
                                lname CHAR(50),
                                mail CHAR(50),
                                number integer,
                                birth_day CHAR(60));''')
            print("We created db")
            if 1==1:
                cursor = conn.cursor()
                fname = str(input("Please input your first name: "))
                lname = str(input("Please input your last name: "))
                mail = str(input("Please input your mail: "))
                number = int(input("Please input your phone number: "))
                birth_day = str(input("Please input your birthday (example: 19 December, 2002): "))
                birth_day_object = datetime.datetime.strptime(birth_day, "%d %B, %Y")
                birth_day_object = str(birth_day_object)
                cursor.execute(
                    "INSERT INTO FORM (fname, lname, mail, number, birth_day) VALUES ('%s', '%s', '%s',%s,'%s')" % (    fname, lname, mail, number, birth_day_object))
                conn.commit()
    else:
        done=True


print("Task 3")
class Animal():# class
    def __init__(self, type, area, lifespan, weight):# is to create objects
        self.type = type
        self.area = area
        self.lifespan = lifespan
        self.weight = weight

    def move(self):# class methods
        return "This %s can move"%self.type
    def eat(self):
        return "This %s eats"%self.type

    def toString(self):
        return f"""type: {self.type}  \ninhabitation area: {self.area}\nlifespan: {self.lifespan}\nweight: {self.weight}\n"""

name = str(input("name of animal: "))
area = str(input("inhabitation area: "))
lifespan = int(input("lifespan: "))
weight = int(input("weight: "))

tiger = Animal(name, area, lifespan, weight)
print(tiger.toString())
print(tiger.move())
print(tiger.eat())

print("Task 4")

class Dog(Animal):# inheritance
    def __init__(self, type, area, lifespan, weight, isTamed, gender):
        super().__init__(type,area, lifespan,weight)# we use parant class __init__
        self.isTamed = isTamed# and else own new parameters
        self.gender = gender

    def sayGaf(self):
        return "gaf gaf gaf"

    def toString(self):
        return f"""type: {self.type}  \ninhabitation area: {self.area}\nlifespan: {self.lifespan}\nweight: {self.weight}\nisTamed: {self.isTamed}\n gender: {self.gender}\n"""
name = "dog"
area = str(input("inhabitation area: "))
lifespan = int(input("lifespan: "))
weight = int(input("weight: "))
isTamed = str(input("isTamed: "))
gender = str(input("gender: "))

dog = Dog(name, area, lifespan, weight, isTamed, gender)
print(dog.toString())
print(dog.move())
print(dog.sayGaf())
print(dog.eat())