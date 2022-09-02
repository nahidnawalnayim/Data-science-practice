#!/usr/bin/env python
# coding: utf-8

# **1st problem**

# In[1]:


print("Hello world")


# **2nd problem**

# In[2]:


A=10
B=9
print(A+B)
A=-10
B=4
print(A+B)
A=15
B=-7
print(A+B)


# **3rd problem**

# In[42]:


R = float(input())
area = (R * R) * 3.14159 
print("A=%0.4f" %area)


# **4th problem**

# In[43]:


A=int(input())
B=int(input())
SOMA=A+B
print(SOMA)


# **5th problem**

# In[44]:


A=int(input())
B=int(input())
PROD=A*B
print(PROD)


# **6th problem**

# In[45]:


A=float(input())
B=float(input())
media=((A*3.5)+(B*7.5))/11
print(f'MEDIA={media:.5f}')


# **7th problem**

# In[47]:


A=float(input())
B=float(input())
C=float(input())
AVG=((A*2)+(B*3)+(C*5))/10
print(f'MEDIA={AVG:.1f}')


# **8th problem**

# In[48]:


A=int(input())
B=int(input())
C=int(input())
D=int(input())
diff=(A*B)-(C*D)
print(diff)


# **9th problem**

# In[49]:


employee_num=int(input());
NUMBER=employee_num
Work_hour=int(input())
amount_per_hour=float(input())
total_salary=Work_hour*amount_per_hour
print(f"NUMBER=",NUMBER);
print(f"SALARY= U$ ",total_salary)


# **10th problem**

# In[50]:


Name=input()
fixed_salary=float(input())
total_sale=float(input());
bonus=float(total_sale*0.15)
total_salary=fixed_salary+bonus
print("TOTAL = R$ %0.2f" %total_salary)


# **11th problem**

# In[7]:


product_1=input().split(" ")
product_2=input().split(" ")
code,qty,price=product_1
code2,qty2,price2=product_2
value_pay=(int(qty)*float(price))+(int(qty2)*float(price2))
print("valor a pagar: R$ %0.2f)" %value_pay)


# **12th problem**

# In[13]:


R=int(input())
sphere_eqn=(4/3)*3.1416*R*R*R
print(f"VOLUME=vol:%0.3f" %sphere_eqn)


# **13th problem**

# In[7]:


A=float(input())
B=float(input())
C=float(input())
area_triangle=1/2*(A*C)
circle_rad=3.1416*(C*C)
trapezium=((A+B)/2)*C
squre=B*B
rectangle=A*B
print("TRIANGULO:%.3f" %area_triangle)
print("CIRCULO:%.3f" %circle_rad)
print("TRAPEZIO:%.3f" %trapezium)
print("QUADRADO:%.3f" %squre)
print("RETANGULO:%.3f" %rectangle)


# **14th problem**

# In[6]:


import math
inputs=input().split(" ")
a,b,c=inputs
eqn=(int(a)+int(b)+abs(int(a)-int(b)))/2
result=(int(eqn)+int(c)+abs(int(eqn)-int(c)))/2
print(result)


# **15th problem**

# In[10]:


X=int(input())
Y=float(input())
consumption=X/Y
print("consumption:%.3f" %consumption)


# **16th problem**

# In[23]:


import math
x1,y1=list(map(float,input().split()))
x2,y2=list(map(float,input().split()))
distance=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("distance:%.4f" %distance)


# **17th problem**

# In[25]:


distance=int(input())
print(f"{distance*2} minutos")


# **18th problem**

# In[30]:


c=int(input())
time=int(input())
speed=int(input())
distance=time*speed
liters_needed=distance/c
print(liters_needed)


# **19th problem**

# In[37]:


notes=int(input())
print(notes)
print(f"R$ 100: {notes/100}")
aux=notes%100
print(aux)


# **20th problem**

# In[38]:


notes = int(input())
print(notes)
print("{} nota(s) de R$ 100,00".format(int(notes/100)))
aux = (notes%100)
print("{} nota(s) de R$ 50,00".format(int(aux/50)))
aux = (aux%50)
print("{} nota(s) de R$ 20,00".format(int(aux/20)))
aux = (aux%20)
print("{} nota(s) de R$ 10,00".format(int(aux/10)))
aux = (aux%10)
print("{} nota(s) de R$ 5,00".format(int(aux/5)))
aux = (aux%5)
print("{} nota(s) de R$ 2,00".format(int(aux/2)))
aux = (aux%2)
print("{} nota(s) de R$ 1,00".format(int(aux/1)))


# **21t problem**

# In[39]:


A,B,C,D= map(int,input().split())

if B>C and D>A and (C+D) > (A+B) and C>0 and D>0 and A%2 ==0:
	print( "Valores aceitos")
else:
	print("Valores nao aceitos")


# **22nd problem**

# In[40]:


import math
A,B,C = map(float,input().split())
D = (B**2)-(4*A*C)
if(D <0 or A==0):
    print("Impossivel calcular")
else:
    D=math.sqrt(D)
    R1 = (-B+D)/(2*A)
    R2 = (-B-D)/(2*A)
    print(f'R1 = {R1:0.5f}\nR2 = {R2:0.5f}')


# **23rd problem**

# In[41]:


X = float(input())
if X>75 and X<=100:
    print("Intervalo (75,100]")
elif X>50 and X<=75:
    print("Intervalo (50,75]")
elif X>25 and X<=50:
    print("Intervalo (25,50]")
elif X>=0 and X<=25:
    print("Intervalo [0,25]")
else:
    print("Fora de intervalo")


# **24th problem**

# In[51]:


X,Y=list(map(int,input().split()))
if(X == 1):
    price  = (float) (4.00 * Y)
elif(X == 2):
    price  = (float) (4.50 * Y)
elif(X == 3):
    price  = (float) (5.00 * Y)
elif (X == 4):
    price  = (float) (2.00 * Y);
elif (X == 5):
    price  = (float) (1.50 * Y)
print(f"Total: R$ {price:.2f}")


# **25TH PROBLEM**

# In[54]:


F1,F2,F3,F4 = map(float,input().split())
F1 = (F1*2+F2*3+F3*4+F4*1)/10
print(f'Media: {F1:.1f}')
if F1>=7.0:
    print("Aluno aprovado.")
elif F1<5.0:
    print("Aluno reprovado.")
elif F1>=5.0 and F1<7.0:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (F1+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')


# **26th problem**

# In[55]:


X,Y=list(map(float,input().split()))
if(X==0 and Y==0):
    print("Origem")
elif(X==0):
    print("Eixo Y")
elif(Y==0):
    print("Eixo X")
elif(X>0 and Y>0):
    print("Q1")
elif(X<0 and Y>0):
    print("Q2")
elif(X<0 and Y<0):
    print("Q3")
elif(X>0 and Y<0):
    print("Q4")


# **27th problem**

# In[56]:


X,Y,Z = map(int,input().split())
list = [X,Y,Z]
list.sort()
print(f"{list[0]}\n{list[1]}\n{list[2]}")
print(f"\n{X}\n{Y}\n{Z}")


# **28th problem**

# In[57]:


A,B,C = map(float,input().split())
if (A+B)>C and (A+C)>B and (B+C)>A:
    perimeter = (A+B+C)
    print(f"Perimetro = {perimeter:0.1f}")
else:
    area = 0.5*(A+B)*C
    print(f"Area = {area:0.1f}")


# **29th problem**

# In[58]:


A,B=map(int, input().split())
if (A%B==0)or(B%A==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")


# **30th problem**

# In[71]:


a,b,c=input().split()
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp
if(a>=(b+c)):
    print("NAO FORMA TRIANGULO")
elif(a*a == (b*b+c*c)):
     print("TRIANGULO RETANGULO")
elif(a * a > (b*b+ c*c)):
    print("TRIANGULO OBTUSANGULO")
elif(a*a<(b*b + c*c)):
    print("TRIANGULO ACUTANGULO")
if(a == b and b == c):
        print("TRIANGULO EQUILATERO")
elif(a == b or b == c):
        print("TRIANGULO ISOSCELES")


# **31th problem**

# In[83]:


a,b=list(map(int,input().split()))
if(a<b):
    time=b-a
else:
    time=b+24-a
print(f"O JOGO DUROU {time} HORA(S)")


# In[ ]:


a,c,b,d=list(map(int,input().split()))

dif=((b*60)+d)-((a*60)+c)
if(dif<=0):
    dif+=24*60
    
time=dif//60
minute=dif%60
print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")


# In[84]:


a = float(input())
if(a>=0 and a<=400):
	b= a*0.15
	c=a+b
	d=15
elif(a>=400.01 and a<=800.00):
	b=a*0.12
	c=a+b
	d=12
elif(a>=800.01 and a<=1200.00):
    b=a*0.1
    c=a+b
    d=10
elif(a>=1200.01 and a<=2000.00):
	b=a*0.07
	c=a+b
	d=7
elif(a>2000):
	b=a*0.04
	c=a+b
	d=4
print(f"Novo salario: {c:.2f}")
print(f"Reajuste ganho: {b:.2f}")
print(f"Em percentual: {d} %")


# In[85]:


x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    animal = 'aguia'
if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    animal = 'pomba'

if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    animal = 'homem'

if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    animal = 'vaca'

if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    animal = 'pulga'

if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    animal = 'lagarta'

if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    animal = 'sanguessuga'

if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    animal = 'minhoca'

print(animal)


# In[86]:


a=int(input())
if a==61:
    print("Brasilia")
elif a==71:
    print("Salvador")
elif a==11:
    print("Sao Paulo")
elif a==21:
    print("Rio de Janeiro")
elif a==32:
    print("Juiz de Fora")
elif a==19:
    print("Campinas")
elif a==27:
    print("Vitoria")
elif a==31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")


# In[87]:


sal = float(input())

if(sal > 0 and sal <= 2000):
 print(f"Isento")
elif(sal > 2000 and sal <= 3000):
 resto = sal - 2000
 resultado = resto * 0.08
 print(f"R$ {resultado:0.2f}")
elif(sal > 3000 and sal < 4500):
 resto = sal - 3000
 resultado = (resto * 0.18) + (1000 * 0.08)
 print(f"R$ {resultado:0.2f}")
else:
 resto = sal - 4500
 resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
 print(f"R$ {resultado:0.2f}")


# In[88]:


x=int(input())
if(x==1):
    print("January")
elif(x==2):
    print("February")
elif(x==3):
    print("March")
elif(x==4):
    print("April")
elif(x==5):
    print("May")
elif(x==6):
    print("June")
elif(x==7):
    print("July")
elif(x==8):
    print("August")
elif(x==9):
    print("September")
elif(x==10):
    print("October")
elif(x==11):
    print("November")
elif(x==12):
    print("December")


# In[89]:


start, end = 1, 100
# iteration
for num in range(start, end + 1):
   # check
   if num % 2 == 0:
      print(num)


# In[90]:


count = 0
for i in range(6):
    nums = float(input())
    if(nums>0):
       count+=1
print(f'{count} valores positivos')


# In[92]:


count=0
for i in range(5):
    n = float(input())
    if(n%2==0):
        count=count+1
print(f"{count} valores pares")


# In[93]:


even=0
odd=0
positive=0
negative=0
for i in range(5):
    n = float(input())
    if(n % 2 == 0):
         even = even+1
    else:
        odd =odd+1
    if (n > 0):
        positive =positive+1
    elif (n < 0):
        negative =negative+1
print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")


# In[94]:


n = int(input())
for i in range(n+1):
    if(i%2==1):
        print(i)


# In[95]:


n=int(input())
i=0
while(i<6):
    if(n%2!=0):
        print(n)
        i=i+1
    n=n+1


# In[96]:


X = int(input())
Y = int(input())
start = min(X,Y)+1
end = max(X,Y)
if start % 2 == 0:
    start += 1

sum = 0
for i in range(start, end, 2):
    sum += i
print(sum)


# In[97]:


X=int(input())
inn=0
out=0
for i in range(0,X):
    N=int(input())
    if(10<=N<=20):
        inn+=1
    else:
        out+=1
print(f"{inn} in")
print(f"{out} out")


# In[98]:


n= int(input())
for i in range(1,n+1):
    if(i%2==0):
        print(f"{i}^2 = {pow(i,2)}")

