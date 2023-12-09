"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 8-Dec-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)

init_mem = {}  # Empty memory at the very beginning

def store(storage, elm):
    storage.update(elm)
    return storage

a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}
mem = store(init_mem, a)
b = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}
mem = store(mem, b)
c = {"00011110101000": [20, 21, 22, 23, 24, 25, 26, 27]}
mem = store(mem, c)
d = {"00111110101000": [30, 31, 32, 33, 34, 35, 36, 37]}
mem = store(mem, d)
e = {"01111110101000": [40, 41, 42, 43, 44, 45, 46, 47]}
mem = store(mem, e)

cache = {
    "blk0": ["00000000000", [0, 0, 0, 0, 0, 0, 0, 0], 0],
    "blk1": ["00000000000", [0, 0, 0, 0, 0, 0, 0, 0], 0],
    "blk3": ["00000000000", [0, 0, 0, 0, 0, 0, 0, 0], 0],
    "blk4": ["00000000000", [0, 0, 0, 0, 0, 0, 0, 0], 0],
}

def fully_ass_cache(cache, adr, storage):
    tag = adr[:7]
    valid_bit = 1
    stag = adr[:11]

    for block_label, block_info in cache.items():
        if block_info[0] == tag and block_info[2] == 1:
            # Hit: Update the values in the cache
            cache[block_label][1] = storage[stag+"000"]
            return cache


    for block_label, block_info in cache.items():
        if block_info[2] == 0:
            cache[block_label] = [tag, storage[stag+"000"], valid_bit]
            return cache


    lru_block = min(cache, key=lambda x: cache[x][2])
    cache[lru_block] = [tag, storage[stag+"000"], valid_bit]
    return cache

print("Initial Cache:", cache)
adr1 = "00000110101010"
cache = fully_ass_cache(cache, adr1, mem)
print("Cache after adr1:", cache)

adr2 = "00001110101010"
cache = fully_ass_cache(cache, adr2, mem)
print("Cache after adr2:", cache)

adr3 = "00011110101111"
cache = fully_ass_cache(cache, adr3, mem)
print("Cache after adr3:", cache)

adr4 = "00111110101101"
cache = fully_ass_cache(cache, adr4, mem)
print("Cache after adr4:", cache)

adr5 = '01111110101110'
cache = fully_ass_cache(cache, adr5, mem)
print("Cache after adr5:", cache)



