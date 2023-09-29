"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 28-SEP-2023
Description : Convert number from any base to any base
"""

from datetime import datetime


def decimal_converter(num):
  while num > 1:
    num /= 10
  return num



def float_bin(number, places=3):

  whole, dec = str(number).split(".")
  whole = int(whole)
  dec = int(dec)

  res = bin(whole).lstrip("0b") + "."

  for x in range(places):

    whole, dec = str((decimal_converter(dec)) * 2).split(".")
    dec = int(dec)
    res += whole

  return res



def floating_model(floating_dec):

  current_dateTime = datetime.now()
  print('\n\nRun Date is ',current_dateTime)

  if not isinstance(floating_dec, float):
    print("Invalid number.")
    return

  binary_str = format(int(floating_dec),"b")
  print('Int',binary_str)

  binary_str2 = float_bin(floating_dec,3)
  print('Float',binary_str2)

  if binary_str2[0] == "-":
     sign = '1'
  else:
     sign = '0'

  exponent = binary_str[0:]
  significand = binary_str2.replace('-0b','')

  significand = significand.replace('.','')

  exponent = int(exponent, 2)
  print('Exponent Int',sign,exponent,significand)

  bias = 2 ** (5 - 1)
  print('Bias is ',bias)

  exponent -= bias
  print('Exponent Bias',sign,exponent,significand)

  exponent_str = format(exponent, "b")
  print('Exponent Binary',exponent_str)

  exponent_str = exponent_str.zfill(5)
  exponent_str = exponent_str[1:6]
  print('Exponent Fill',exponent_str)

  converted_num = sign + "_" + exponent_str + "_" + significand
  print('Output of Float to Binary for ', floating_dec, " is ",  converted_num )

  return converted_num


# Example usage:

# Convert the number 26.625 to 14-bit binary floating-point.
floating_model(-26.625)
floating_model(26.625)

