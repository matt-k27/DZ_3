print('DZ3')

inputtedNumber = int(input('Enter your number pls : '))

numerator, denominator = divmod(inputtedNumber, 10000)
outputNumber = numerator

numerator, denominator = divmod(denominator, 1000)
outputNumber += numerator*10

numerator, denominator = divmod(denominator, 100)
outputNumber += numerator*100

numerator, denominator = divmod(denominator, 10)
outputNumber += numerator*1000

numerator, denominator = divmod(denominator, 1)
outputNumber += numerator*10000

print(outputNumber)


print('Thank you for using')