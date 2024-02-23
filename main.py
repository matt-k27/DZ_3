print('DZ3')

inputtedNumber = int(input('Enter your number pls : '))

numerator, denominator = divmod(inputtedNumber, 10)
outputNumber = str(denominator)
numerator, denominator = divmod(numerator, 10)
outputNumber += str(denominator)
numerator, denominator = divmod(numerator, 10)
outputNumber += str(denominator)
numerator, denominator = divmod(numerator, 10)
outputNumber += str(denominator)
numerator, denominator = divmod(numerator, 10)
outputNumber += str(denominator)

print(outputNumber)

############################################

print(str(inputtedNumber)[::-1])

print('Thank you for using')