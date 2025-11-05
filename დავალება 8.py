print("დავალება 8")

# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

# ფიბონაჩის მიმდევრობის ფორმულა F(n) = F(n-1) + F(n-2)  როდესაც n ≥ 2

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(0)) 
print(fibonacci(1))
print(fibonacci(2))  
print(fibonacci(7))

# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება,რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.

def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


print(anagram("listen", "silent"))  
print(anagram("apple", "  papel"))

# მომხმარებელმა რომ კონსოლიდან შეიტანოს სიტყვების მნიშვნელობა

def is_anagram(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


word1 = input("შეიყვანეთ სიტყვა: ")
word2 = input("შეიყვანეთ სიტყვა: ")

if is_anagram(word1, word2):
    print("ანაგრამებია")
else:
    print("არ არის ანაგრამა")


# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.  (n!=n×(n−1)×(n−2)×⋯×2×1)

def factorial(n):

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(3))
print(factorial(4))


# 4. დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.

def symbol(text, symbol):
    
    count = 0
    for ch in text:
        if ch == symbol:
            count += 1
    return count


print(symbol("mariam", "a")) 
             


