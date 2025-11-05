print("დავალება 6")

print("studentebis ID: 20, 25, 56, 100, 1232, 846723")


my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}


# მთლიანი სიის გამოტანა 

for student in my_dict.get('students'):
  st_id = student['id']
  st_name = student['name']
  st_age = student['age']
  st_grade = " "
  
  
  print(f" ID: {st_id}, Name: {st_name}, Age: {st_age}, Grade: {st_grade}")
  
  
  for subject in my_dict["subjects"]:
    grades = subject["grades"]
    if st_id in grades: 
        print(f"Subject: {subject['name']}, Grade: {grades[st_id]}")
        
       

# კონკრეტული ID ის მიხედვით ქულების გამოტანა


for student in my_dict.get('students'):
    st_id = str(student['id']) 
    st_name = student['name']
    st_age = student['age']

    print(f" ID: {st_id}, Name: {st_name}, Age: {st_age}")

    for subject in my_dict["subjects"]:
        grades = subject["grades"]
        if st_id in grades: 
            print(f"Subject: {subject['name']}, Grade: {grades[st_id]}")


student_id = input("\nაირჩიეთ სტუდენტის ID: ")


selected_student = None
for s in my_dict["students"]:
    if str(s["id"]) == student_id:
        selected_student = s
        break


if selected_student:
    print(f"Student Information:ID: {selected_student['id']}, Name: {selected_student['name']}, Age: {selected_student['age']}")
    print("Grades:")
    for subject in my_dict["subjects"]:
        grade = subject["grades"].get(student_id)
        if grade:
            print(f"Subject: {subject['name']}, Grade: {grade}")
else:
    print("ასეთი ID არ მოიძებნა.")