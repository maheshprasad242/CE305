"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 17-OCT-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)


def filler(a, b):
    output = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            output.append('0')
        else:
            output.append('1')

    return ''.join(output)


def modfn(dividend, divisor):
    ldiv = len(divisor)

    tmp = dividend[0: ldiv]

    while ldiv < len(dividend):

        if tmp[0] == '1':
            tmp = filler(divisor, tmp) + dividend[ldiv]
        else:
            tmp = filler('0' * ldiv, tmp) + dividend[ldiv]

        ldiv += 1

    if tmp[0] == '1':
        tmp = filler(divisor, tmp)
    else:
        tmp = filler('0' * ldiv, tmp)

    output = tmp
    return output

def encoding(msg, poly):
    print(msg,poly)
    l_poly = len(poly)
    appended_msg = msg + '0' * (l_poly - 1)
    remainder = modfn(appended_msg, poly)

    output = msg + remainder
    return output

print('\nEncoding')
print('Output is ',encoding('1010','100101'))
print('Output is ',encoding('1100','100101'))

def decoding(rcv, poly):
    l_poly = len(poly)
    remainder = modfn(rcv, poly)
    print(rcv,poly)
    if int(remainder) == 0:
        return 'No Error'
    else:
        return 'Error'

print('\nDecoding')

print(decoding('101000111','100101'))
print(decoding('110011111','100101'))