#25pt

print "How many numbers do you want to add together?"

userInput = int(raw_input())

total = 0

for x in range(userInput):
    print "Enter a number."
    userInput2 = int(raw_input())
    total = total + userInput2
    
print total

#50pt

print "How many numbers do you want to add together?"

userInput = int(raw_input())

totalCost = []

for x in range(userInput):
    print "Enter a number."
    userInput2 = int(raw_input())
    totalCost.append(userInput2)
print sum(totalCost)

#75pt

print "What number do you want to take the factorial of?"

userInput = int(raw_input())

factorial = 1

for x in range(1, userInput + 1, 1):
    factorial = factorial * x
    
print "The answer is " + str(factorial)

#100pt

print "What number do you want to find the factors of?"

factor = []

userInput = int(raw_input())

for x in range(1, userInput + 1, 1):
# [ 1,2,3,....userInput]
    if userInput % x == 0:   
        factor.append(x)

print "The answer is " + str(factor)