print("დავალება")

print("მე-10 ლექციის დავალება")

def flatten(arg):
  for item in arg:
    if isinstance(item, (list, tuple, set, frozenset)):
      yield from flatten(item)
    elif isinstance(item, dict):
      yield from flatten(item.values())
    else:
      yield item



arr = [1, 2, 3, [[4, 5, 6], "Text", 7], {'title': 'The wolf', 'pages': 256}, (8, [9, 0], True, {5, 8, False})]

arr = list(flatten(arr))

print(*arr)

print("დავალება 10")

# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']

print(list(zip(arr1, arr2)))


# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

# params:[1, 2, 3, 4, 5] 
# output: 120

from functools import reduce

def multiply_num(numbers):
    try:
        return reduce(lambda x, y: x * y, numbers)
    except TypeError:
        return "შეიყვანეთ რიცვხები"
print(multiply_num([1, 2, 3, 4, 5]))
 
# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

arr1 = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in arr1 if x % 2 != 0]
print(odds)

# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']


def ending(words, ending):
    
    try:
        
        result = list(filter(lambda word: isinstance(word, str) and word.endswith(ending), words))
        return result
    except TypeError:
        return "პარამეტრი უნდა იყოს სია ან სტრიქონი"
    except Exception as e:
        return f"შეცდომა: {e}"


print(ending(['hello', 'world', 'coding', 'nod'], 'ing'))