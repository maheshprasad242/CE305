"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 28-SEP-2023
Description : Convert number from any base to any base
"""

from datetime import datetime

def base_conv(num, base, new_base):

  current_dateTime = datetime.now()
  print('\n\nRun Date is ',current_dateTime)

  res = [int(i) for i in num.split('-') if i.isdigit()]
  print('\nInput is ', res,' in base ', str(base),'Convert to new base ',new_base)
  first = [int(d) for d in str(res[0])]
  #print(res, first)
  res = first + res[1:]
  res.reverse()
  print('Reverse',res)

 # Check if the number is valid.
  print('Validating Input')
  for digit in res[0:]:
    print('Checking if ',str(digit), ' is less than ', str(base))
    if  digit > base:
        print('\nInvalid Number: Aborting\n')
        return
  print('Validating ok')


  print('Changing to base 10')

  decimal_num = 0
  i = 0
  for digit in res:
    decimal_num += digit * base**i
    decimal_cnum = digit * base ** i
    print(str(digit),' * ',str(base),' ^ ',str(i),' = ',str(decimal_cnum),' Total = ',str(decimal_num))
    i+=1

  print('Decimal base', str(decimal_num))
  print('Changing to base', str(new_base))

  new_base_num = ""
  while decimal_num > 0:
    print(str(decimal_num),' / ', str(new_base))
    remainder = decimal_num % new_base
    new_base_num += str(remainder)+'-'
    decimal_num //= new_base
    print('Quotient = ',str(decimal_num), ' Remainder = ', str(remainder), )


  print('New Base Num is', new_base_num)
  ores = [int(i) for i in new_base_num.split('-') if i.isdigit()]
  ores.reverse()
  print('New Base Num Reversed is',ores)
  my_string = ''

  for digit in ores:
    my_string += str(digit) +  '-'

  print('\nOutput in base ',str(new_base),' is ', my_string[:-1])
  return new_base_num



base_conv("123-45-6", 44, 23)
base_conv("123-45-6", 46, 23)
base_conv("6-54-3-21", 46, 23)
base_conv("6-54-3-21", 63, 74)