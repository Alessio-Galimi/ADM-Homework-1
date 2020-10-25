# Problem1
#Introduction
#Ex1_Say_Hello_World_with_Python
    print("Hello, World!")

#Ex2_Python_If_Else
import math
import os
import random
import re
import sys
n = int(input())
if n < 1 or n > 100 :
    print ("Invalid Input") 
elif n % 2 == 1 or n<=20 and n >=6 :
    print("Weird") 
else :
    print("Not Weird")   
         
#Ex3_Arithmetic_Operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

#Ex4_Python_Division
a = int(input())
b = int(input())
print(a//b)
print(a/b)

#Ex5_Loops
n = int(input())
a = 0
while a < n:
    print(a**2)
    a = a + 1

#Ex6_Write_a_function
def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True  
    return leap
year = int(input())
print(is_leap(year))

#Ex7_Print_function
n = int(input())
for i in range(1,n+1):
    print(i, end="", sep="")

#Data_Types
#Ex1_List_Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())
l = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
l.sort()
print(l)

#Ex2_Find_the_runner_up_score
n = int(input())
arr = [int(z) for z in input().split()]
arr = list(set(arr))
max_value = max(arr)
arr.remove(max_value)
runner_up_value = max(arr)
print(runner_up_value)

#Ex3_Nested_lists
n = int(input())
python_students = list()
for i in range(n):
    name = input()
    score = float(input())
    student = [name, score]
    python_students.append(student)
score_set =set([student[1] for student in python_students])
score_set.remove(min(score_set))
second_lowest_score = min(score_set)
sls_students= [student[0] for student in python_students if student[1] == second_lowest_score]
sls_students.sort()
for student in sls_students :
    print(student)

#Ex4_Finding_the_percentage
n = int(input())
student_marks = {}
for i in range(n):
    line = [(x) for x in input().split()]
    name = line[0]
    marks = line[1:]
    student_marks[name] = marks
query_name = input()
query_name_marks = student_marks[query_name]
average_mark = sum(float(i) for i in query_name_marks)/len(query_name_marks)
print ("%0.2f" % average_mark)

#Ex5_Lists
N = int(input())
l = list()
for n in range(N):
    line = input().split()
    if line[0] == "insert":
        l.insert(int(line[1]), int(line[2]))
    elif line[0] == "print":
        print(l)
    elif line[0] == "remove":
        l.remove(int(line[1]))
    elif line[0] == "append":
        l.append(int(line[1]))
    elif line[0] == "sort":
        l.sort()
    elif line[0] == "pop":
        l.pop()
    else:
        l.reverse()

#Ex6_Tuples
n = int(input())
string_list = input().split()
integer_list = (int(x) for x in string_list)
integer_tuple = tuple(integer_list)
print(hash(integer_tuple))

#Strings
#Ex1_Swap_case
def swap_case(s):
    swapped_string = str()
    for n in range(len(s)):
        if s[n].isalpha():
            if s[n].isupper():
                z = str(s[n].lower())
                swapped_string = swapped_string + z
            elif s[n].islower():
                z = str(s[n].upper())
                swapped_string = swapped_string + z
        else:
            z = str(s[n])
            swapped_string = swapped_string + z
    return swapped_string
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#Ex2_String_Split_and_Join
def split_and_join(line):
    line = line.split()
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Ex3_What_is_your_name
def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python." )

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Ex4_Mutations
def mutate_string(string, position, character):
    mutated_string = string[0:position] + character + string[position+1:]
    return mutated_string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Ex5_find_a_string
def count_substring(string, sub_string):
    substring_length = len(sub_string)
    occurrences = 0
    for i in range(len(string)):
        if string[i:substring_length+i] == sub_string:
            occurrences = occurrences + 1
    return occurrences

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#Ex6_string_validators
s = input()
x = False
for i in range(len(s)):
    if s[i].isalnum():
        x = True
print(x)
x = False
for i in range(len(s)):
    if s[i].isalpha():
        x = True
print(x)
x = False
for i in range(len(s)):
    if s[i].isdigit():
        x = True
print(x)
x = False
for i in range(len(s)):
    if s[i].islower():
        x = True
print(x)
x = False
for i in range(len(s)):
    if s[i].isupper():
        x = True
print(x)

#Ex7_Text_alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Ex8_text_wrap
import textwrap

def wrap(string, max_width):
    l = textwrap.fill(string, max_width)
    return l

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Ex9_Designer_door_mat
n,m = (int(i) for i in input().split())
for i in range(1,n,2):
    print("-"*((m-(i*3))//2) + ".|."*i + "-"*((m-(i*3))//2))
print("-"*((m-7)//2)+"WELCOME"+"-"*((m-7)//2))
for i in range(1,n,2):
    i= n-i-1
    print("-"*((m-(i*3))//2) + ".|."*i + "-"*((m-(i*3))//2))

#Ex10_String_formatting
def print_formatted(number):
    width=(len(bin(number))) - 2
    for i in range(1, number + 1):
        a =str(i)
        b=oct(i)[2:]
        c=hex(i)[2:]
        c=c.upper()
        d=bin(i)[2:]
        print(" "*(width-len(a)) + a," "*(width-len(b)) + b," "*(width-len(c))+c," "*(width-len(d)) + d)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)         

#Ex11_Alphabet_rangoli
def print_rangoli(size):
    for i in range(size):
        print("-"*((size-i-1)*2), end='')
        for n in range(i+1):
            if size==1:
                print(chr(97-n+size-1), end='')
            else:   print(chr(97-n+size-1) +("-"), end='')
        for l in range(i):
            if l == i-1 and i == size-1:
                print(chr(97+l-i+size), end='')
            else:print(chr(97+l-i+size) +("-"), end='')
        print("-"*((size-i-1)*2-1))
    for i in range(1, size):
        i=size-i-1
        print("-"*((size-i-1)*2), end='')
        for n in range(i+1):
            print(chr(97-n+size-1) +("-"), end='')
        for l in range(i):
            print(chr(97+l-i+size) +("-"), end='')
        print("-"*((size-i-1)*2-1))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)   
        
#Ex12_Capitalize
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if s[0].isalpha():
        z=s[0].upper()
        s=z+s[1:]
    for i in range (1, len(s)):
        if s[i-1] == " " and s[i].isalpha():
            z=s[i].upper()
            s=s[:i]+z+s[i+1:]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#Ex13_the_minion_game
def minion_game(string):
    stuart_points = 0
    kevin_points = 0
    for i in range(len(s)):
        if s[i] in ("A,E,I,O,U"):
            kevin_points = kevin_points + len(s) - i
        else: 
            stuart_points = stuart_points + len(s) - i
    if stuart_points> kevin_points:
        print("Stuart",stuart_points)
    elif stuart_points< kevin_points:
        print("Kevin",kevin_points)
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

#Ex14_Merge_the_tools
def merge_the_tools(string, k):
    while len(string) !=0:
        i = 0
        str_k = string[:k]
        while i <len(str_k):
            character=str_k[i]
            index= str_k.find(character,i+1)
            if index != -1:
                str_k= str_k[:index]+str_k[index+1:]
            else: i = i+1
        print(str_k)
        string = string[k:]
         
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#Sets
#Ex1_Introduction_to_sets
def average(array):
    sum_ = sum(set(array))
    len_ =len(set(array))
    return (sum_/len_)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#Ex2_No_idea
a = input()
array = list(map(int,input().split()))
A_ =set(map(int, input().split()))
B_ =set(map(int, input().split()))
happiness = 0
for i in array:
    if i in A_:
        happiness = happiness +1
    elif i in B_:
        happiness = happiness - 1
print(happiness)

#Ex3_Symmetric_difference
n_a=int(input())
values_a = set(map(int,input().split()))
n_b=int(input())
values_b = set(map(int,input().split()))
union_ =values_a.union(values_b)
intersection_= values_a.intersection(values_b)
sym_=union_.difference(intersection_)
sym_=sorted(sym_)
for i in sym_:
    print(i)

#Ex4_set_add
n=int(input())
countries_=set()
for i in range(n):
    country_ =input()
    countries_.add(country_)
print(len(countries_))

#Ex5_set_discard_remove_pop
n = int(input())
s = set(map(int, input().split()))
n_commands =int(input())
for i in range(n_commands):
    command= input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))

#Ex6_set_union
a =int(input())
eng_=set(input().split())
b=int(input())
fre_=set(input().split())
tot_ =eng_.union(fre_)
print(len(tot_))

#Ex7_set_intersection
a =int(input())
eng_=set(input().split())
b=int(input())
fre_=set(input().split())
int_=eng_.intersection(fre_)
print(len(int_))

#Ex8_set_difference
a =int(input())
eng_=set(input().split())
b=int(input())
fre_=set(input().split())
diff_=eng_.difference(fre_)
print(len(diff_))

#Ex9_set_symmetric_difference
a =int(input())
eng_=set(input().split())
b=int(input())
fre_=set(input().split())
sym_=eng_.symmetric_difference(fre_)
print(len(sym_))

#Ex10_set_mutations
a=input()
s=set(map(int,input().split()))
n =int(input())
for i in range(n):
    command=input().split()
    s2=set(map(int,input().split()))
    if command[0]== "intersection_update":
        s.intersection_update(s2)
    if command[0]== "update":
        s.update(s2)
    if command[0]== "difference_update":
        s.difference_update(s2)
    if command[0]== "symmetric_difference_update":
        s.symmetric_difference_update(s2)
print(sum(s))   

#Ex11_the_captain_room
k=int(input())
l=input().split()
s1 =set(l[:len(l)//2])
s2 =set(l[len(l)//2:])
s=s1.symmetric_difference(s2)
for i in s:
    if l.count(i)==1:
        print(i)

#Ex12_check_subset
n=int(input())
for i in range(n):
    n_a=int(input())
    s_a=set()
    l_a=input().split()
    for a in l_a:
        s_a.add(a)
    n_b=int(input())
    s_b=set()
    l_b=input().split()
    for b in l_b:
        s_b.add(b)
    print(s_a.issubset(s_b))

#Ex13_Check_strict_supersect
set_a=set(map(int,input().split()))
n = int(input())
superset_= True
for i in range(n):
    set_b=set(map(int,input().split()))
    set_diff= set_a.difference(set_b)
    if not (set_b.issubset(set_a) and len(set_diff)!=0):
        superset_=False
print(superset_)

#Collections
#Ex1_Collections_Counter
a=int(input())
shoe_sizes=list(map(int,input().split()))
n= int(input())
money_earned=0
for i in range(n):
    customer=list(map(int,input().split()))
    if customer[0] in shoe_sizes:
        money_earned=money_earned+customer[1]
        shoe_sizes.remove(customer[0])
print(money_earned)

#Ex2_DefaultDict_tutorial
from collections import defaultdict
numbers_=list(map(int,input().split()))
a=list()
b=list()
for i in range(numbers_[0]):
    a.append(input())
for j in range(numbers_[1]):
    b.append(input())
d=defaultdict(list)
for i in range(len(a)):
    d[a[i]].append(i+1)
for j in b:
    s=str()
    for i in d[j]:
        s=s+str(i)+" "
    s.rstrip()
    if len(s)==0:
        print(-1)
    else: print(s)

#Ex3_collections_namedtuple
from collections import namedtuple
n=int(input())
column_names=input().split()
total_sum=0
tuple_=namedtuple("tuple_",column_names)
for i in range(n):
    column_=input().split()
    p=tuple_(column_[0],column_[1],column_[2],column_[3])
    mark=int(p.MARKS)
    total_sum=total_sum+mark
print(round((total_sum/n),2))

#Ex4_Collections_OrderedDict
from collections import OrderedDict
n=int(input())
ord_dict={}
for i in range(n):
    s=input().split()
    item_name=str()
    for l in range(len(s)-1):
        item_name=item_name+s[l]+" "
    item_name= item_name.rstrip()
    price=int(s[len(s)-1])
    if item_name in ord_dict:
        new_price = ord_dict[item_name]+price
        ord_dict[item_name]=new_price
    else: ord_dict[item_name]=price
for i in ord_dict:
    print(i, ord_dict[i])

#Ex5_word_order
from collections import OrderedDict
n=int(input())
ord_dict={}
for i in range(n):
    word=input()
    if word in ord_dict:
        occurrences= ord_dict[word]+1
        ord_dict[word]=occurrences
    else: ord_dict[word]= 1
print(len(ord_dict))
for i in ord_dict:
    print(ord_dict[i],end=" ")

#Ex6_collections_deque
from collections import deque
d = deque()
n=int(input())
for i in range(n):
    s=input().split()
    if s[0]=="append":
        d.append(s[1])
    if s[0]=="appendleft":
        d.appendleft(s[1])
    if s[0]=="pop":
        d.pop()
    if s[0]=="popleft":
        d.popleft()
for i in d:
    print(i,end=" ")

#Ex7_Company_logo
import math
import os
import random
import re
import sys
from collections import OrderedDict

if __name__ == '__main__':
    s = input()
    s.strip()
    s=sorted(s)
    d=dict()
    logo=OrderedDict()
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    values=set(d.values())
    while len(logo)<3:
        max_=max(values)
        for i in d:
            if d[i]==max_:
                logo[i]=d[i]
                if len(logo)==3:
                    break
        values.remove(max_)    
for i in logo:
    print(i, logo[i])

#Ex8_piling_up
from collections import deque
n=int(input())
for i in range(n):
    a=int(input())
    numbers_=deque(map(int,input().split()))
    possible=True
    base_value=max(numbers_)
    while len(numbers_)>0 and possible:
        if numbers_[0]>=numbers_[len(numbers_)-1] and numbers_[0]<=base_value:
            base_value=numbers_[0]
            numbers_.popleft()
        elif numbers_[len(numbers_)-1]<=base_value:
            base_value=numbers_[len(numbers_)-1]
            numbers_.pop()
        else:
            possible = False
    if possible:
        print("Yes")
    else: print("No")        

#Date_and_Time
#Ex1_Calendar_module
from datetime import date
date_=list(map(int,input().split()))
n = date(date_[2],date_[0],date_[1]).weekday()
if n == 0:
    print("MONDAY")
elif n == 1:
    print("TUESDAY")
elif n == 2:
    print("WEDNESDAY")
elif n == 3:
    print("THURSDAY")
elif n == 4:
    print("FRIDAY")
elif n == 5:
    print("SATURDAY")
else: print("SUNDAY")

#Ex2_Time_Delta
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_time=list(map(int,t1[16:24].split(":")))
    t2_time=list(map(int,t2[16:24].split(":")))
    t1_time[0]=t1_time[0]-int(t1[25:28])
    t2_time[0]=t2_time[0]-int(t2[25:28])
    t1_time[1]=t1_time[1]-int(t1[25]+t1[28:])
    t2_time[1]=t2_time[1]-int(t2[25]+t2[28:])
    hours_diff=(t1_time[0]-t2_time[0])*3600 +(t1_time[1]-t2_time[1])*60 + (t1_time[2]-t2_time[2])
    s_t1=t1[4:15]
    date_t1= datetime.strptime(s_t1,'%d %b %Y')
    s_t2=t2[4:15]
    date_t2 = datetime.strptime(s_t2,'%d %b %Y')
    days_diff= (date_t1-date_t2)
    days_diff=days_diff.total_seconds()
    tot_diff=abs(int(hours_diff+days_diff))
    return str(tot_diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Exceptions
#Ex1_Exceptions
n=int(input())
for i in range(n):
    try:
        l=list(map(int,input().split()))
        print(l[0]//l[1])
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

#Built_ins
#Ex1_Zipped
n=list(map(int,input().split()))
n_students=n[0]
n_subjects=n[1]
l_marks=list()
for i in range(n_subjects):
    l=list(map(float,input().split()))
    l_marks.append(l)
z=zip(*l_marks)
for i in z:
    s=0
    for j in range(n_subjects):
        s=s+i[j]
    print(s/n_subjects)

#Ex2_Athlete_sort
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    list_k=list()
    for i in arr:
        list_k.append(i[k])
    list_k.sort()
    list_ord=list()
    for i in list_k:
        for j in arr:
            if i ==j[k] and j not in list_ord:
                list_ord.append(j)
    for i in list_ord:
        s=str()
        for j in range(m):
            s=s+str(i[j])+" "
        s=s.strip()
        print(s)

#Ex3_ginortS
s=str(input())
uppercase_list=list()
lowercase_list=list()
odd_list=list()
even_list=list()
for i in s:
    if i.isalpha():
        if i.isupper():
            uppercase_list.append(i)
        else:lowercase_list.append(i)
    else:
        if int(i)%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
uppercase_list.sort()
lowercase_list.sort()
odd_list.sort()
even_list.sort()
s_uppercase=str()
s_lowercase=str()
s_odd=str()
s_even=str()
for i in uppercase_list:
    s_uppercase=s_uppercase+str(i)
for i in lowercase_list:
    s_lowercase=s_lowercase+str(i)
for i in odd_list:
    s_odd=s_odd+str(i)
for i in even_list:
    s_even=s_even+str(i)
print(s_lowercase+s_uppercase+s_odd+s_even)

#Python_functionals
#Ex1_Map_and_Lambda_function
cube = lambda x: x*x*x
def fibonacci(n):
    fib_list=list()
    n1=0
    n2=1
    if n ==1:    
        fib_list.append(n1)
    elif n>1:
        fib_list.append(n1)
        fib_list.append(n2)
        for i in range(2,n):
            n3=n1+n2
            fib_list.append(n3)
            n1=n2
            n2=n3
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#Regex_and_Parsing
#Ex1_detect_floating_point_number
n=int(input())
for i in range(n):
    s=input()
    if s[0] =="+" or s[0]=="-":
        s=s[1:]
    if "." in s:
        x=s.find(".")
        s=s[0:x]+s[x+1:]
        if s.isdigit():
            print("True")
        else: print("False")
    else: print("False")

#Ex2_Re_split
regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Ex3_Group_Groups_Groupdict
s=input()
not_found=True
not_last=True
i=0
while not_found and not_last:
    if i ==len(s)-2:
        not_last=False
    if s[i].isalnum() and s[i]==s[i+1]:
        not_found = False
        print(s[i])
    else: i = i +1
if not_found: print("-1")

#Ex4_Re_findall_Re_finditer
import re
s=input()
z=str()
found=False
for i in range(len(s)):
    if s[i] in "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm":
        z=z+"!!"
    else: z=z+s[i]
l= re.findall(r'[!][AEIOUaeiou]+[!]',z)
for i in l:
    if len(i)>3:
        print(i[1:len(i)-1])
        found=True
if not found:
    print("-1")

#Ex5_Re_start_Re_end
import re
s=input()
k=input()
c=0
if k in s:
    while k in s:
        m = re.search(k,s)
        start_index=m.start()
        end_index=m.end()-1
        tuple_=(start_index +c,end_index+c)
        print(tuple_)
        s=s[start_index+1:]
        c=c+start_index+1
else:(print("(-1, -1)"))

#Ex6_Regex_Substitution
import re

n=int(input())
for i in range(n):
    z=input()
    x= re.sub("((?<= )[&][&](?= ))", "and", z)
    l=re.sub("((?<= )[|][|](?= ))", "or", x)
    print(l)

#Ex7_Validating_Roman_Numerals
regex_pattern = r"\AM{,3}(CM|CD|D?C{,3})(XC|XL|L?X{,3})(IX|IV|V?I{,3})\Z"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Ex8_Validating_Phone_Numbers
import re
n=int(input())
for i in range(n):
    num=input()
    float_ =bool(re.search(r"\A(7|8|9){1}(9|8|7|6|5|4|3|2|1|0){9}\Z",num))
    if float_:
        print("YES")
    else:print("NO")

#Ex9_Validating_and_Parsing_Email_addresses
import re
n=int(input())
for i in range(n):
    l =input()
    valid = bool(re.search(r"([a-zA-Z])+( <){1}([a-zA-Z]){1}([a-zA-Z0-9\-\.\_])+(@){1}([a-zA-Z])+[.]{1}([a-zA-Z]){1,3}(>){1}",l))
    x= (re.search(r"([a-zA-Z])+( <){1}([a-zA-Z]){1}([a-zA-Z0-9\-\.\_])+(@){1}([a-zA-Z])+[.]{1}([a-zA-Z]){1,3}(>){1}",l))
    if valid:
        print(x.group())

#Ex10_Hex_Color_Code
import re
n=int(input())
for i in range(n):
    line=input()
    if line != "" and line[0]!="#":
        codes=re.findall(r"#[0-9a-fA-f]{3}[0-9a-fA-F]{,3}",line)
        for i in codes:
            print(i)

#Ex11_HTML_parser_part_1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for i in attrs:
            if len(i)==1:
                print("->",i[0],">", "None")
            elif len(i)>1:
                print("->",i[0],">", i[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for i in attrs:
            if len(i)==1:
                print("->",i[0],">", "None")
            elif len(i)>1:
                print("->",i[0],">", i[1])
parser = MyHTMLParser()
n=int(input())
for i in range(n):
    l=input()
    parser.feed(l)

#Ex12_HTML_Parser_part_2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data and data !="\n":
            print(">>> Multi-line Comment","\n"+data)  
        elif "\n" not in data and data !="\n":
            print(">>> Single-line Comment","\n"+data)
    def handle_data(self, data):
        if data !="\n":
            print(">>> Data","\n"+data)    

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Ex13_Detect_HTML_Tags_Attributes_AttributesValues
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for i in attrs:
            print("->", i[0],">" ,i[1])
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for i in attrs:
           print("->", i[0],">" ,i[1])

parser = MyHTMLParser()
n=int(input())
for i in range(n):
    l=input()
    parser.feed(l)

#Ex14_Validating_UID
import re
n=int(input())
for i in range(n):
    uid=input()
    valid_10_char =bool(re.search(r"[a-zA-Z0-9]{10}",uid))
    code = re.search(r"[a-zA-Z0-9]{10}",uid)
    code=code.group()
    for z in code:
        if code.count(z) >1:
            valid_10_char=False
    code = re.findall(r"[A-Z]",uid)
    if len(code)<2:
            valid_2_alpha=False
    else:
        valid_2_alpha=True
    code = re.findall(r"[0-9]",uid)
    if len(code)<3:
            valid_3_digits=False
    else:
        valid_3_digits=True
    
    if valid_10_char and valid_2_alpha and valid_3_digits:
        print("Valid")
    else:print("Invalid")

#Ex15_Validating_Credit_Card_Numbers
import re
n=int(input())
for i in range(n):
    valid=True
    l=input()
    number= re.fullmatch(r"([4-6]{1})([0-9]{3})(\-{0,1})([0-9]{4})([\-]{0,1})([0-9]{4})([\-]{0,1})([0-9]{4})",l)
    if not number:
        valid=False
    else:
        s=number.group(0)
        for k in range(16):
            if s[k] == "-":
                s=s[:k]+s[k+1:]
        for m in range(13):
            if s[m]==s[m+1] and s[m+1]==s[m+2] and s[m+2]==s[m+3]:
                valid=False
                break
    if valid:
        print("Valid")
    else: print("Invalid")

#Ex16_Validating_postal_codes
regex_integer_in_range = r"\A[1-9]{1}[0-9]{4}[0-9]{1}\Z"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Ex17_Matrix_script
import re
n=input().split()
rows=int(n[0])
columns=int(n[1])
s=" "*(rows*columns)
for i in range(rows):
    l=input()
    for k in range(columns):
        s= s[:k*rows+i]+l[k]+s[k*rows+1+i:]
x=re.sub(r"([a-zA-Z0-9]{1})[!@#$%& ]{1,}([a-zA-Z0-9]{1})",r"\1 \2",s)
print(x)

#XML
#Ex1_Find_the_score
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    n=0
    for i in node.iter():
        d=(i.attrib)
        n=n+len(d)
    return n

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#Ex2_Find_the_maximum_depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if len(elem)>0:
        level =level + 1
        if level==maxdepth:
            maxdepth = maxdepth+1
        for i in elem:
            depth(i, level)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#Decorations
#Ex1_Standardize_mobile_numbers_using_decorators
def wrapper(f):
    def fun(l):
        numbers=list()
        for i in l:
            if len(i)==13:
                z="+91 "+i[3:8]+" "+i[8:]
            elif len(i)==12:
                z="+91 "+i[2:7]+" "+i[7:]
            elif len(i)==11:
                z="+91 "+i[1:6]+" "+i[6:]
            elif len(i)==10:
                z="+91 "+i[:5]+" "+i[5:]
            numbers.append(z)
        return f(numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#Ex2_Name_directory
import operator
def person_lister(f):
    def inner(people):
        l=sorted(people, key=lambda x: int(x[2]))
        return map(f,l)
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#Numpy
#Ex1_Arrays
import numpy

def arrays(arr):
    rev_arr=list()
    for i in range(len(arr)):
        rev_arr.append(arr[len(arr)-i-1])
    np_rev_arr=numpy.array(rev_arr,float)
    return np_rev_arr

    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Ex2_Shape_and_Reshape
import numpy
l=list(input().split())
arr=numpy.array(l,int)
arr.shape=(3,3)
print(arr)

#Ex3_Transpose_and_Flatten
import numpy
v=input().split()
n = int(v[0])
m = int(v[1])
l=list()
for i in range(n):
    line=input().split()
    l.append(line)
l=numpy.array(l,int)
print(numpy.transpose(l))
print(l.flatten())

#Ex4_Concatenate
import numpy
l=input().split()
n=int(l[0])
m=int(l[1])
p=l[2]
l1=list()
l2=list()
for i in range(n):
    line=input().split()
    l1.append(line)
arr1=numpy.array(l1,int)
for i in range(m):
    line=input().split()
    l2.append(line)
arr2=numpy.array(l2,int)
print (numpy.concatenate((arr1, arr2)))

#Ex5_Zeros_and_ones
import numpy
n=list(map(int,input().split()))
print (numpy.zeros(n,dtype = numpy.int))
print(numpy.ones(n,dtype = numpy.int))

#Ex6_Eye_Identity
import numpy
l=input().split()
n=int(l[0])
m=int(l[1])
z= numpy.eye(n,m,0)
z= str(z).replace("1", " 1").replace("0"," 0")
print(z)

#Ex7_array_mathematics
import numpy
l=input().split()
n=int(l[0])
m=int(l[1])
l1=list()
l2=list()
for i in range(n):
    line=input().split()
    l1.append(line)
arr1=numpy.array(l1,int)
for i in range(n):
    line=input().split()
    l2.append(line)
arr2=numpy.array(l2,int)
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)

#Ex8_Floor_ceil_rint
import numpy
numpy.set_printoptions(sign=' ')
l=input().split()
a=numpy.array(l,float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

#Ex9_sum_and_prod
import numpy
numpy.set_printoptions(sign=' ')
l=input().split()
n=int(l[0])
m=int(l[1])
l1=list()
for i in range(n):
    line=input().split()
    l1.append(line)
arr1=numpy.array(l1,int)
print(numpy.prod(numpy.sum(arr1,axis=0)))

#Ex10_Min_and_Max
import numpy
numpy.set_printoptions(sign=' ')
l=input().split()
n=int(l[0])
l1=list()
for i in range(n):
    line=input().split()
    l1.append(line)
arr1=numpy.array(l1,int)
print(numpy.max(numpy.min(arr1,axis=1)))

#Ex11_Mean_Var_Std
import numpy
numpy.set_printoptions(legacy='1.13')
l=input().split()
n=int(l[0])
l1=list()
for i in range(n):
    line=input().split()
    l1.append(line)
arr1=numpy.array(l1,int)
print(numpy.mean(arr1,axis=1))
print(numpy.var(arr1,axis=0))
print(numpy.std(arr1))

#Ex12_Dot_and_Cross
import numpy
numpy.set_printoptions(sign=' ')
l=input().split()
n=int(l[0])
l1=list()
l2=list()
for i in range(n):
    line=input().split()
    l1.append(line)
arr1=numpy.array(l1,int)
for i in range(n):
    line=input().split()
    l2.append(line)
arr2=numpy.array(l2,int)
print(numpy.dot(arr1,arr2))

#Ex13_Inner_and_Outer
import numpy
numpy.set_printoptions(sign=' ')
A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))

#Ex14_polynomials
import numpy
pol = list(map(float,input().split()))
x=float(input())
print(numpy.polyval(pol,x))

#Ex15_Linear_Algebra
import numpy
l=input().split()
n=int(l[0])
l1=list()
for i in range(n):
    line=input().split()
    l1.append(line)
arr1=numpy.array(l1,float)
result=numpy.linalg.det(arr1)
result=round(result,2)
print(result)

#Problem2
#Ex1_Birthday_cake_candles
import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_height=max(candles)
    tallest_candles=0
    for i in candles:
        if i ==max_height:
            tallest_candles=tallest_candles+1
    return tallest_candles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Ex2_Number_line_jumps
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    possible=False
    if v1>v2:
        while x2>x1:
            x1=x1+v1
            x2=x2+v2
            if x1==x2:
                possible=True
    if possible:
        return "YES"
    else: return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Ex3_Viral_Advertising
import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared=5
    liked=(shared//2)
    cumulative=liked
    for i in range(n-1):
        shared=liked*3
        liked=(shared//2)
        cumulative=cumulative+liked
    return cumulative        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Ex4_Recursive_Digit_Sum
import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    n=str(n)
    digit_sum=0
    for i in n:
        digit_sum=digit_sum+int(i)
    if digit_sum%9==0:
        return 9
    else: 
        remainder=digit_sum%9
        new_remainder= remainder*k
        if new_remainder%9==0:
            return 9
        else: return new_remainder%9

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#Ex5_Insertion_sort_part1
import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    value=arr[n-1]
    l=n-2
    while arr[l]>value and l>=0:
        arr[l+1]=arr[l]
        l=l-1
        s=str()
        for i in arr:
            s=s+str(i)+" "
        print(s)
    arr[l+1]=value
    s=str()
    for i in arr:
        s=s+str(i)+" "
    print(s)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Ex6_Insertion_sort_part_2
import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for z in range (1,n):
        value=arr[z]
        l=z-1
        while arr[l]>value and l>=0:
            arr[l+1]=arr[l]
            l=l-1
        arr[l+1]=value
        s=str()
        for i in arr:
            s=s+str(i)+" "
        print(s)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



