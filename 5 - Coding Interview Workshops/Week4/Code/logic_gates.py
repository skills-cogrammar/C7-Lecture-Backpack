#Logic gates

#NOT gate
def NOT(a):
    return not a
print('NOT(1):',NOT(1))
print('NOT(0)',NOT(0))
#Output: false, true

#AND gate
def AND (a, b):
 
    if a == 1 and b == 1:
        return True
    else:
        return False
print('1 AND 0',AND(1, 0))
print('1 AND 1',AND(1, 1))
#Output: false, true

#OR gate    
def OR(a, b):
    if a == 1 or b ==1:
        return True
    else:
        return False
print('0 AND 0',OR(0, 0))
print('0 AND 1',OR(0, 1))
#Output: false, true

#XOR gate    
def XOR (a, b):
    if a != b:
        return True
    else:
        return False

print('1 XOR 1:',XOR(1,1))
print('1 XOR 0:',XOR(1,0))
#Output: false, true
 
# print("+---------------+----------------+")
# print(" A = False, B = False | A AND B =",AND(False,False)," | ")
# print(" A = False, B = True | A AND B =",AND(False,True)," | ")
# print(" A = True, B = False | A AND B =",AND(True,False)," | ")
# print(" A = True, B = True | A AND B =",AND(True,True)," | ")