print("დავალება 9")

 # 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც  მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

int_list = [10,20,30,40]

def my_number(num):
    global int_list
    int_list.append(num)
    return int_list

print(my_number(80))

# 2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

def sum_numbers(num):
    return sum(num)

my_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

print(sum_numbers(my_list))

# 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს.

gl_str = "Global"

def global_function():
    gl_str = "Local"
    return gl_str


print("ლოკალური ცვლადი", global_function())

# 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს  ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).

def sum_numbers(number):
    

    if number < 10:
        return number
    else:
        
        return sum_numbers(number // 10) + number % 10

print(sum_numbers(12345))

# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH)


def string(s):

    if len(s) <= 1:
        return s
    
    else :
        return s[-1] + string(s[:-1])
    
print(string("Hello"))  





