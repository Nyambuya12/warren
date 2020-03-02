print('KUDAKWASHE MARAMBA H180389W')

# inputting Credit card number

Credit_Card_Number = input('Enter the credit card number number you want to check its validity ')

a = 0
Sum = 0

# double the value of every second digit in the credit card

for a in range(0, len(Credit_Card_Number), 2):
    b = int(Credit_Card_Number[a])
    b = b + b
# evaluating the credit card number to see whether it is greater than 9
    if b >= 10:
       c = str (b)
       Sum = int (c[0] + c[1])

    else:
        Sum = Sum + b
t = 0

# adding the remainder values into the total

for t in range(1, len(Credit_Card_Number), 2):
    f = int(Credit_Card_Number[t])
    Sum += f

    result = str(Sum)
# checking if the credit card number is valid

    if result[1] == '0':
        print("valid")
    else:

        print("invalid")

    print('4137 8947 1175 5904 = valid')
    print('6499 8024 5027 3568 = invalid')
    print('8504 1721 9127 3888 = valid')
    print('0043 6687 8348 5480 = invalid')

