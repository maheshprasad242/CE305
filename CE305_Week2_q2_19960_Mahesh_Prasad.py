"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 17-OCT-2023
"""

from datetime import datetime

current_dateTime = datetime.now()
print('\n\nRun Date is ', current_dateTime)

import numpy as np

def ExtraParityBits(m):

    for i in range(m):
        if( 2**i >= m + i + 1):
            return i

def HamEncoding(msg):
    m=len(msg)
    k = ExtraParityBits(m)
    print('Input Sig = ', msg, ' Calculated k = ', k )
    msgOut = []
    parity = []
    binPos = [bin(x)[2:] for x in range(1, k + len(msg) + 1)]

    msgOrd = []
    msgG = []
    qtdBP = 0
    contmsg = 0

    for x in range(1, k + len(msg) + 1):
        if qtdBP < k:
            if (np.log(x) / np.log(2)).is_integer():
                msgG.append("P")
                qtdBP = qtdBP + 1
            else:
                msgG.append("D")
        else:
            msgG.append("D")

        if msgG[-1] == "D":
            msgOrd.append(msg[contmsg])
            contmsg += 1
        else:
            msgOrd.append(None)

    qtdBP = 0
    for bp in range(1, k + 1):
        contBO = 0
        contLoop = 0
        for x in msgOrd:
            if x is not None:
                try:
                    aux = (binPos[contLoop])[-1 * (bp)]
                except IndexError:
                    aux = "0"
                if aux == "1":
                    if x == "1":
                        contBO += 1
            contLoop += 1
        if contBO % 2 == 0:
            parity.append(0)
        else:
            parity.append(1)

        qtdBP += 1

    ContBP = 0
    for x in range(0, k + len(msg)):
        if msgOrd[x] is None:
            msgOut.append(str(parity[ContBP]))
            ContBP += 1
        else:
            msgOut.append(msgOrd[x])
    print('Encoded Output is : ',''.join(msgOut))
    return


def HamDecoding(arr,nr):
    print('\nReceived Sig is ',arr,' k = ', nr)
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])


        res = res + val * (10 ** i)

    correction = int(str(res), 2)
    if (correction == 0):
        print("No error")
    else:
        error_position = len(arr) - correction + 1
        print("Error as position", error_position)
        corrected = list(arr)

        if corrected[error_position-1] == '0':
            corrected[error_position-1] = '1'
        else:
            corrected[error_position-1] = '0'

        print('Corrected String is ', ''.join(corrected))
    return


print('\nEncoding')
HamEncoding('1101')
HamEncoding('1001011')

print('\n\nDecoding')
HamDecoding('1010101',3)
HamDecoding('1010001',3)

