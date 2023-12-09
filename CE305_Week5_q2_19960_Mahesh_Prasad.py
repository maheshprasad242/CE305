"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 8-Dec-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

init_mem = {}


def store(storage, elm):
    storage.update(elm)
    return storage

a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}
mem = store(init_mem, a)

b = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}
mem = store(mem, b)

c=    {"00001110111000":[20,21,22,23,24,25,26,27]}
mem = store(mem, c)

cache_size = 16
block_size = 8

cache1={}

cache={"0000": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "0001": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "0010": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "0011": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "0100": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "0101": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "0110": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "0111": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1000": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1001": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1010": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1011": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1100": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1101": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1110": ["0000000", [0,0,0,0,0,0,0,0], 0],
       "1111": ["0000000", [0,0,0,0,0,0,0,0], 0]}


def dir_map_cache(cache, adr, storage):

    cache_index = adr[7:11]
    tag = adr[:7]
    stag = adr[:11]

    if cache[cache_index][2] == 1:
        print("Storage Occupied")
    else:
        cache[cache_index][0] = tag
        cache[cache_index][1] = storage[stag + "000"]
        cache[cache_index][2]  = 1

    return cache

def check_cache(cache, adr):

    cache_index = adr[7:11]
    tag = adr[:7]

    if cache_index in cache and cache[cache_index][2] == 1 and cache[cache_index][0] == tag:
        print("Hit")
    else:
        print("Miss")
    return cache

adr1    = "00000110101010"
cache = dir_map_cache(cache, adr1, mem)

print("Checking address:", adr1)
check_cache(cache, adr1)

adr2 = "00001110101010"
cache = dir_map_cache(cache, adr2, mem)
print("Checking address:", adr2)
check_cache(cache, adr2)

adr3 = "00001110111111"
cache = dir_map_cache(cache, adr3, mem)
print("Checking address:", adr3)
check_cache(cache, adr3)



