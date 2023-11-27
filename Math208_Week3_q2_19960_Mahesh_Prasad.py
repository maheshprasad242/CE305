"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 27-Nov-2023
Description : Convert number from any base to any base
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

import numpy as np

p_A = 0.6
p_B = 0.4

N = np.arange(4, 8)
p_N = np.zeros(N.shape)
p_N[0] = (p_A ** 4) * (p_B ** 3)
p_N[1] = (p_A ** 5) * (p_B ** 2) + 4 * (p_A ** 4) * (p_B ** 3) * p_A
p_N[2] = (p_A ** 6) * p_B + 6 * (p_A ** 5) * (p_B ** 2) * p_A + 4 * (p_A ** 4) * (p_B ** 3) * p_A ** 2
p_N[3] = (p_A ** 7) + 7 * (p_A ** 6) * p_B + 21 * (p_A ** 5) * (p_B ** 2) * p_A + 35 * (p_A ** 4) * (p_B ** 3) * p_A ** 2

E_N = np.sum(N * p_N)

print("Probability distribution of N:",N, " is ", p_N)
print("Expected value of N:",E_N)


