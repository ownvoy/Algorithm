import sys
from typing import final
input = sys.stdin.readline

parentheses = input().strip()

one_hot_vector = []
laser_num = 0
i= 0
while(i <=len(parentheses)-1):
    if(parentheses[i] == '('  and parentheses[i+1] == ')'):
        laser_num += 1
        one_hot_vector.append(0)
        i += 2
    elif(parentheses[i] == '('):
        one_hot_vector.append(1)
        i+=1
    else:
        one_hot_vector.append(2)
        i+=1
# print(one_hot_vector)
original_line = (len(parentheses)- 2*laser_num)/2

temp = 0
final_line = original_line
j = 0
while(len(one_hot_vector)):
    if(one_hot_vector[j] == 0):
        one_hot_vector.pop(j)
        final_line += temp
        
    elif(one_hot_vector[j] == 1):
        temp += 1
        j+=1
    else:
        temp-= 1
        one_hot_vector.pop(j)
        one_hot_vector.pop(j-1)
        j-= 1


print(int(final_line))
