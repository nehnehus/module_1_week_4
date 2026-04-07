# Reverse a String assignment:
# Used hashtags after running the code to make sure each one worked.

#def reversed_string(s):

#    return s[::-1]
#result = reversed_string("hello")
#print(result)


#def reversed_string(s):
 #   reversed_s = ""
 #   for char in s:
 #       reversed_s = char + reversed_s
 #   return reversed_s
#result = reversed_string("Python")
#print(result)

#def reversed_string(s):
   # return s [::-1]
#original = "hello"
#reversed_str = reversed_string(original)
#print(f"Original: {original}, Reversed: {reversed_str}")


#import string

#def reversed_string(data, ignore_special=False):
#if ignore_special and isinstance(data, str):
        
#filtered_data = [char for char in data if char.isalnum()]
#return data[::-1]
#print(f"String:{reversed_string("Hello, World!")}")
#print(f"Filtered: {reversed_string("Hello, World!", True)}")
#print(f"List: {reversed_string([1, 2, 3, 4, 5])}")

#Check for a Palindrome:
#import re
#def ispalindrome(s: str) -> bool:
 #   normalized_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
 #   reversed_s = normalized_s[::-1]
 #   return normalized_s == reversed_s
#print(ispalindrome("A man, a plan, a canal: Panama"))
#print(ispalindrome("racecar"))
#print(ispalindrome("hello"))


#Find the maximum number in a list:

#def find_max(numbers):
 #   if not numbers:
 #       return None
 #   current_max = numbers[0]
 #   for number in numbers[1:]:
  #      if number > current_max:
  #          current_max = number
  #  return current_max

#num_list1 = [4, 9, 1, 17, 2]
#max_value1 = find_max(num_list1)
#print(f"The maximum value in {num_list1} is {max_value1}")

#num_list2 = [-5, -9, -2, -12]
#max_value2 = find_max(num_list2)
#print(f"The maximum value in {num_list2} is {max_value2}")

#num_list3 = [42]
#max_value3 = find_max(num_list3)
#print(f"The maximum value in {num_list3} is {max_value3}")

#Challenge: Prime Time

#def is_prime(n):
    #if n <= 1:
       # return False
   # if n == 2:
       # return True
    #for i in range(2, int(n**0.5) + 1):
      #if n % i  == 0:
         #return False

    #return True
#print(f"2: {is_prime(2)}")
#print(f"11: {is_prime(11)}")
#print(f"15: {is_prime(15)}")
#print(f"1: {is_prime(1)}")
#print(f"0: {is_prime(0)}")

#Challenge: Caesar Cipher Encoder

#def caesar_cipher(text, shift):
    #result = ""
    #shift = shift % 26 
    #for char in text:
        #if char.isalpha():
           # start = ord('A') if char.isupper() else ord('a')
            #new_char = chr(start + (ord(char) - start + shift) % 26)
            #result += new_char
        #else:
            #resut += char

    #return result
#message = "abc"
#print(caesar_cipher(message, 3))
#message = "xyz"
#print(caesar_cipher(message, 2))

#print(caesar_cipher("Hello, World!", 5))

#Challenge: Count Word Frequency in a Text File

#import string
#def count_word_frequencies(filename):
    #word_counts = {}
    #try:
        #with open(filename, 'r') as file:
            #for line in file:
                #line = line.lower()
                #line = line.translate(str.maketrans('', '', string.punctuation))
                #words = line.split()
                #for word in words:
                    #word_counts[word] = word_counts.get(word, 0) + 1
        #return word_counts
    #except FileNotFoundError:
        #return "Error: The file was not found."
#with open ('practice.txt', 'w') as f:
    #f.write('The cat and the hat.')
#result = count_word_frequencies('practice.txt')
#print(result)

#Challenge: Write and Save a Simple Log File

#import datetime
#def log_activity():
   #message = input("Enter a message on activity:")
   #now = datetime.datetime.now()
   #timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   #log_entry = f"[{timestamp}] {message}\n"
   #try:
    #with open("log.txt", "a") as file:
        #file.write(log_entry)
    #print("Activity successfully logged to log.txt.")
   #except Exception as e:
    #print(f"An error occurred: {e}")
#def read_log():
    #print("\n--- Log Contents---")
    #try:
        #with open("log.txt", "r") as file:
            #print(file.read())
    #except FileNotFoundError:
        #print("Log file does not exist yet.")

#if __name__ == "__main__":
   #log_activity()
   #read_log()
   
#Challenge: Build a Basic Calculator

#import math
#def add(a, b):
    #return a + b
#def subtract(a, b):
    #return a - b
#def multiply(a, b):
    #return a * b
#def divide(a, b):
    #if b == 0:
        #raise ValueError("Cannont divide by zero.")
    #return a / b
#def exponent(a, b):
    #return a ** b
#def modulus(a, b):
   #if b == 0:
        #raise ValueError("Cannot perform modulus by zero.")
    #return a % b
#def log_calculation(operation, n1, n2, result):
    #with open("calc_history.txt", "a") as f:
        #f.write(f"{n1} {operation} {n2} = {result}\n")
#def main():
   # operations = {
        #'1': ('+', add),
        #'2': ('-', subtract),
        #'3': ('*', multiply),
        #'4': ('/', divide), 
        #'5': ('**', exponent),
        #'6': ('%', modulus)
    #}
    #while True:
        #print("\n---Menu Driven Calculator---")
       # print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent\n6. Modulus")
        #print("Type 'exit' to quit.")
        #choice = input("Select an operation (1-6): ").strip().lower()
        #if choice == 'exit':
            #print("Goodbye!")
            #break
        #if choice not in operations:
            #print("Invalid choice. Please try again.")
            #continue
        #try:
            #num1 = float(input("Enter first number: "))
            #num2 = float(input("Enter second number:"))    
            #symbol, func = operations[choice] 
            #result = func(num1, num2)
            #print(f"Result: {result}")
            #log_calculation(symbol, num1, num2, result)
        #except ValueError as e:
            #print(f"Error: {e if str(e) else 'Please enter valid numbers.'}") 
        #except Exception as e:
            #print(f"An unexpected error occured: {e}")   
#if __name__ == '__main__':
    #main()

#Challenge: Password Strength Checker

#def check_password_strength(password):
    #length_ok = len(password) >= 8
    #has_upper = any(char.isupper() for char in password)
    #has_lower = any(char.islower() for char in password)
    #has_digit = any(char.isdigit() for char in password)
    #has_symbol = any(not char.isalnum() for char in password)

    #missing = []
    #if not length_ok: missing.append("minumum 8 characters")
    #if not has_upper: missing.append("uppercase letter")
    #if not has_lower: missing.append("lowercase letter")
    #if not has_digit: missing.append("number")
    #if not has_symbol: missing.append("symbol")

    #total_met = 5 - len(missing)

    #if total_met == 5:
        #return "Strong"
    #elif total_met >= 3:
        #return f"Medium (missing{', '.join(missing)})"
    #else:
        #return f"Weak (missing{', '.join(missing)})"
#user_password = input("Enter a password: ")
#result = check_password_strength(user_password)
#print(f"Result: {result}")

#Challenge: FizzBuzz with a Twist

#for i in range(1, 101):
    #output = ""
    #if i % 3 == 0:
        #output += "Fizz"
    #if i % 5 == 0:
        #output += "Buzz"
    #if i % 7 == 0:
        #output += "Bang"
    #print(output if output else i)


