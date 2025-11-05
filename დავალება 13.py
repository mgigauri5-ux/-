print("დავალება 13")

import os, csv
 
path = "files"

filename = "data2.csv"

os.makedirs(path, exist_ok=True)

filename = os.path.join(path, filename)

data = [
    ["id", "name", "age", "grade", "subject_name", "mark"],
    [1, "string", 0, "string", "string", 0],
    [2, "string", 0, "string", "string", 0]
]

with open(filename, mode='w', encoding='utf-8', newline="") as file:
  
  writer = csv.writer(file)
  writer.writerows(data)

print("ფაილის შექმნა")

# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფორმაციას(id,name,age,grade,subject_name,mark) და თქვენ სტუდენტს დაამატებს csv ფაილში. დაასორტირეთ მონაცემები id-ის მიხედვით.

import os, csv

def add_student():

    file_name = "data_student.csv"
    
    student_id = int(input("შეიყვანეთ ID: "))
    name = input("შეიყვანეთ სახელი: ")
    age = int(input("შეიყვანეთ ასაკი: "))
    grade = input("შეიყვანეთ კლასი: ")
    subject_name = input("შეიყვანეთ საგანი: ")
    mark = float(input("შეიყვანეთ ნიშანი: "))
    
    new_student = [student_id, name, age, grade, subject_name, mark]
    
    try:
        
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = list(csv.reader(file))
            header = reader[0]
            rows = reader[1:]

    except FileNotFoundError:
        header = ["id", "name", "age", "grade", "subject_name", "mark"]
        rows = []

    rows.append(new_student)

    
    rows.sort(key=lambda x: int(x[0]))

   
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print("სტუდენტი დაემატა")

add_student()


# 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან

import os, csv

def read_student_info(file_name="data_student.csv", student_id=None):
    
    if not os.path.exists(file_name):
        print(f"ფაილი '{file_name}' არ არსებობს.")
        return
    
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students = list(reader)
        
    if not students:
        print("ინფო არ არის")
        return

    if student_id is None:
        print("ყველა სტუდენტი:")
        for student in students:
            print(student)
    else:
        found = False
        for student in students:
            if str(student["id"]) == str(student_id):
                print(f"სტუდენტის ინფორმაცია ID={student_id}:")
                print(student)
                found = True
                break
        if not found:
            print(f"სტუდენტი ID={student_id} not found")


read_student_info("data_student.csv")
read_student_info("data_student.csv", student_id=2)

# 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.


import csv

def average_marks(file_name="data_student.csv"):
    
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                subject = row["subject"]
                try:
                    mark = float(row["mark"])
                    subject[subject].append(mark)
                except ValueError:
                    continue

            if not subject:
                print("CSV ფაილი ცარიელია.")
                return

            print("საშუალო:")
            for subject, marks in subject.items():
                avg = sum(marks) / len(marks)
                print(f"{subject}: {avg:.2f}")

    except FileNotFoundError:
        print(f"ფაილი '{file_name}' არ არსებობს.")
    except Exception as e:
        print(f"შეცდომა: {e}")


# 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.

import csv, os

def update_mark(file_name="data_student.csv"):

    if not os.path.exists(file_name):
        print(f"ფაილი '{file_name}' არ არსებობს.")
        return

    try:
        student_id = input("სტუდენტის ID: ").strip()
        subject_name = input("საგანი ").strip()
        new_mark = float(input("ნიშანი, ახალი: "))
    except ValueError:
        print("მონაცემები არ არის სწორი")
        return

    updated = False
    students = []

    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["id"] == student_id and row["subject_name"].lower() == subject_name.lower():
                row["mark"] = str(new_mark)
                updated = True
            students.append(row)

    if not updated:
        print(f"სტუდენტი ID={student_id} საგან '{subject_name}' ვერ მოიძებნა.")
        return

    with open(file_name, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "name", "age", "grade", "subject_name", "mark"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print(f" ID={student_id}'{subject_name}'განახლდა.")

