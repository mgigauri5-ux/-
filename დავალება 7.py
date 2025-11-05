print("დავალება 7")

# 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set)


set1 = set()
print(type(set1))

arr = [19, 28, 20, 15, 12]

set1 = set(arr)

print(set1)

# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, რომლის შეცვლაც შეუძლებელი იქნება (frozenset).

my_set = {1, 2, 3, 4}
my_frozenset = frozenset(my_set)
print(my_frozenset)

# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

combined_set = set1 | set2
combined_tuple = tuple(combined_set)
print(combined_tuple)

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).

my_tuple = (1, 2, 2, 5, 6, 8, 9, 9)

my_list = list(set(my_tuple))
print(my_list)

# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:

# [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# დაბეჭდეთ შემდეგი ფორმატით:

# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11

list_people = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for name, age in list_people:
    print(f"Name: {name}, Age: {age}")

#მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]დავბეჭდოთ თანხვედრა.

my_list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
my_list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]


print(set(my_list1)-set(my_list1).difference(set(my_list2)))













