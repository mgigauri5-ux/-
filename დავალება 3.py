n =int(input("შეიყვანეთ რიცხვი"))

sum_numbers = 0

for i in range(1, n + 1):
    sum_numbers += i

print(sum_numbers)    

print()



n =int(input("შეიყვანეთ რიცხვი"))

while n > 0:
    print(n)
    n -=1

print()




from random import randint

num = randint(1,100)

i = 1

print("guess")

while True:
    guess = int(eval(input(f"step #{i}. Your guess: ")))

    if guess == num:
        print(f"you guess it was {num}.")
        break
    elif guess > num:
        print("too great")
    else:
        print("too less")    

    print() 

print("game over")


total_sum = 0

while True:
    
    user_number = input("შეიყვანეთ რიცხვი")

    if user_number == "sum":
        print(total_sum)
        break
    else:
        number = int(user_number)
        if number > 0:
            total_sum += number
            



