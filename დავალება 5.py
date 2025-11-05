print("დავალება 5")

print("Task1")

import sys

my_list = []

while True:

    text = input("შეიყვანეთ რომელიმე ანბანის ასო")

    if text == 'a':
        
        num = input("შეიყვანეთ ნულისგან განსხვავებული რიცხვი: ")
        if num.isdigit():
            my_list.append(int(num))
            print(num)
        else:("შეყვანილი ტექსტი არასწორია")

    elif text == 'r':

        num = input("შეიყვანეთ რიცხვი: ")
        if num.isdigit():
            num = int(num)
            if num in my_list:
                my_list.remove(int(num))
                print(num)

        else:("შეყვანილი ტექსტი არასწორია")
    
    elif text == 'e': 
        sys.exit()       

    else:
        print("შეყვანილი ტექსტი არასწორია") 
        break


print("Task2")

my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

print(my_list_1.index(210))


#ამატებს ბოლოში

my_list_1.append("hello")
print(my_list_1, "\n")

#ამატებს ბოლო ელემენტში

print(len(my_list_1)-1)
my_list_1[len(my_list_1)-1].append("hello")
print(my_list_1)

my_list_1.pop(2)
print(my_list_1, "\n")

my_list_2 = my_list_1
my_list_2.clear
print(my_list_1)
print(my_list_2)


print("Task2")

import re

phone1 = "(123) 456-789"

pattern = r"\(\d{3}\) \d{3}-\d{3}"

print(re.fullmatch(pattern, phone1))