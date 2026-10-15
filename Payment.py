# print("hello world from python")

balance = 5000
print("Welcome to PKA!")

# Enter the shopping amount
amount =int( input("Enter your amount :"))

if (amount <= 0):
    print("Invalid amount")

elif amount > balance:
    print("Insufficient balance")

elif amount == balance:
    print("Payment successful! Your account is empty now")

else:
    print("Payment successful")