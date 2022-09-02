# 1st problem
print("Hello, world!")

# 2nd problem
a = int(input())
b = int(input())
print (a + b)
print (a - b)
print (a * b)

# 3rd problem
a = int(input())
b = int(input())

print(a // b)
print(a / b)

#4th problem

N = int(input())
for i in range(N):
    print (i * i)

#5th problem

def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))

#6th problem

Result =[]
scorelist = []
32

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 

    for a,c in sorted(Result):
        if c==b:
            print(a)

#7th problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);    

#8th problem
tuple_len = int(input())
a = tuple(map(int, input().split(' ')))
print (hash(a))

#9th problem
def split_string(string):
    list_string = string.split(' ')
    return list_string
def join_string(list_string):
    string = '-'.join(list_string)
    return string
if __name__ == '__main__':
    string = 'this is a string'
    list_string = split_string(string)
    new_string = join_string(list_string)
    print(new_string)

#10th problem
def swap_case(s):   
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

