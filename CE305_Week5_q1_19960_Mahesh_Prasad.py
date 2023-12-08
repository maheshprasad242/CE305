"""
Stuent Name : Mahesh Prasad (Id : 19960)
College     : SFBU
Date        : 8-Dec-2023
"""

from datetime import datetime
current_dateTime = datetime.now()
print('\n\nRun Date is ',current_dateTime)


init_mem = {}  # Empty memory at the very beginning

a = {800: 123}  # 1st data with address 800 and value 123
b = {900: 1000}  # 2nd data with address 900 and value 1000

def store(storage, elm):  # Store an element to the memory
    storage.update(elm)
    return storage


mem = store(init_mem, a)
print('Added a', mem)

mem = store(mem, b)
print('Added b',mem)

c = {800: 900}
mem = store(mem, c)
print('Added c',mem)

d = {1500: 700}
mem = store(mem, d)
print('Added d',mem)

def imm_load_ac(val):
    global ac
    ac = val
    return ac

ac = imm_load_ac(800)
print('ac after imm_load',ac)

def dir_load_ac(storage, val):
    global ac
    ac = storage.get(val, 0)
    return ac


ac = dir_load_ac(mem, 800)
print('ac after dir_load',ac)

def indir_load_ac(storage, val):
    global ac
    indirect_address = storage.get(val, 0)
    ac = storage.get(indirect_address, 0)
    return ac

ac = indir_load_ac(mem, 800)  # ac = 1000
print('ac after indir_load',ac)

def idx_load_ac(storage, idx, val):  # Load accumulator(ac) by Indexed addressing
    global ac
    idxreg = idx
    address = val + idxreg
    ac = storage.get(address, 0)
    return ac

ac = idx_load_ac(mem, 700, 800)  # ac = 700
print('ac after idx_load',ac)
