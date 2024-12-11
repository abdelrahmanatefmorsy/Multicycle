from classes import *
import re
s = "add  $t0 , $t1 , $t2"
Registers = [
    "$zero",
    "$v0", "$v1", 
    "$a0", "$a1", "$a2", "$a3",
    "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7",
    "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7",
    "$t8", "$t9"
]
def r_type(instruction):
    if(len(instruction) != 4):
        print("invalid instruction")
    if(instruction[0] in ["sll","srl"]):
        pass
    else:
        if (instruction[1] in Registers and instruction[2] in Registers and instruction[3] in Registers):
            for j in Fetch:
                j.make_active()
        else:
            print(instruction[1:])
    


code = [(["add,sub,and,or,sll,srl", lambda instruction: r_type(instruction)])]
lst = re.split(r'[ ,]+', s)
for i in code:
    if lst[0] in i[0]:
        i[1](lst)
