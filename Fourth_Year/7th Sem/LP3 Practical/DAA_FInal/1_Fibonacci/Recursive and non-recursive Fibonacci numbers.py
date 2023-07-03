# Fibonacci Series using Non-recursive method
first_num = int(input("Enter the first number of the fibonacci series: "))
second_num = int(input("Enter the second number of the fibonacci series: "))
num_of_terms = int(input("Enter the number of terms:"))

# Fibonacci Series using recursive method
def fibonacci(first_num):
	if first_num <= 1:
		return first_num
	return fibonacci(first_num-1) + fibonacci(first_num-2)

print("The numbers in fibonacci series using Recursive Method are : ")
for i in range(num_of_terms):
   print(fibonacci(i))

# Fibonacci Series using Non-recursive method
if num_of_terms <= 0:
   print("Plese enter a positive integer")
print("The numbers in fibonacci series using Non-Recursive Method are : ")
print(first_num)
print(second_num)
while(num_of_terms-2):
   third_num = first_num + second_num
   first_num=second_num
   second_num=third_num
   print(third_num)
   num_of_terms=num_of_terms-1







