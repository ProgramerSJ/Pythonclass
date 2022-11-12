#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World !!!")


# In[3]:


money = True

if money == True: # 같은 지 물어보기 위해서는 == 두 개
    print("택시를 타자")
else : 
    print("걸어 가자")


# In[7]:


money = 8000

if money >= 5000:
    print("택시를 타자")
elif money >= 1000:
    print("버스를 타자")
else :
    print("걸어 가자")


# In[16]:


# 학생의 성적을 입력 받아서, 
# 점수가 90 이상이면 "A학점 입니다."
# 점수가 80 이상이면 "B학점 입니다."
# 점수가 70 이상이면 "C학점 입니다."
# 점수가 60 이상이면 "D학점 입니다."
# 나머지는 모두 "F 학점입니다."

score = int(input("성적을 입력하세요 : "))

if score >= 90:
    print("A학점 입니다.")
elif score >= 80:
    print("B학점 입니다.")
elif score >= 70:
    print("C학점 입니다.")
elif score >= 60:
    print("D학점 입니다.")
else :
    print("E학점 입니다.")


# In[2]:


# While

no = 10

while no>= 0: # no 이 0보다 큰가? => 10~0까지 출력
    print(no)
    no = no - 1


# In[2]:


prompt = "1. 덧셈 / 2. 뺄셈 / 3. 곱셈 / 4. 나눗셈 / 5. 종료"
no = 0

while no <= 4 :
    print(prompt)
    no = int(input())
    
# for가 더 어울리는 case


# In[7]:


no = 0

while no <= 7: # 이 부분에서 0보다 큰 경우가 아닌 10 이하인 경우로 실행한다면..
    print(no)
    no = no + 1 # 이 경우 무한반복이 되기 때문에, 중간에 정지시킬 필요가 있음.


# In[8]:


no = 0

while True: # True의 경우에도 무한 반복됨.
    print(no)
    no = no + 1
    
    if no > 9:
        break # While 문의 종료(빠져나가는 명령어)


# In[24]:


no = 1
sum = 0

while no < 100: # 1번째 while 1~100 범위 내 숫자
    if no % 3 == 0 : # 조건 1. 숫자는 3으로 나눈 나머지가 0
        sum = sum + no # 합은 = 숫자들의 합
        no = no + 1 # 숫자 는 1씩 증가
    
    else:
        no = no + 1 # 그 외에는 숫자는 1씩 증가
print("1부터 100까지 3의 배수의 합은 :", sum)


# In[27]:


#Solution
no = 1
sum = 0

while no <=100:
    if no % 3 == 0 :
        sum = sum + no
        
    no = no + 1 #자신의 자신을 하나 증가하는 표현은 no += 1, java 에서는 no++;
    
print("1부터 100까지의 3의 배수의 합은 :", sum)


# In[33]:


# For 구문
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)


# In[41]:


math = [80, 90, 70, 70, 100] # for 문에서의 5가지 요소를 가진 리스트

j = 1 # j는 1부터의 숫자
for i in math :# i는 math 에서인데,
    if i >= 90: # 만약 90점 이상이면 
        print(j,"번째 학생은 합격입니다.") #리스트의 j번째 학생은~
    else:
        print(j,"번째 학생은 불합격입니다.")
    j += 1


# In[43]:


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)


# In[47]:


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i % 2 == 0 :
        print(i)


# In[48]:


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i % 2 != 0:
        continue # 밑으로 내려가지 않고 다시 반복문의 진행
        
    print(i)


# In[ ]:


# range 함수 (for 문 과 잘 맞음, while에서는 거의 쓸 필요는 없음.)

# 숫자를 자동으로 생성해줌. for 문과 함께 사용되는 경우가 아주 많음.


# In[50]:


print(range(1,11))


# In[52]:


for i in range(1,11): #두 번째 수는 미만을 의미함.
    print(i)


# In[58]:


#for 문으로 구구단 출력하기

for i in range(2, 10): 
    for j in range(1, 10): 
        print(i, "*", j, "=", i*j, end="\t") 
    print()   


# In[60]:


for i in range(2, 10): #i는 단을 표현
    for j in range(1, 10): # 이중 for문은 자주 사용됨. 2차원대로 넘어감.
        print(i*j, end="\t") # 2단까지 다 돌았을 때,
    print() #한 단마다 줄 바꾸기


# In[106]:


for i in range(2, 10): 
    for j in range(1, 10): 
        print(i,"*",j,"=", i*j, end="\t\n") # 1단이 끝날 때, 탭과 줄바꿈을 사용
    print() # 한 단마다 줄 바꾸기


# In[132]:


# range를 사용하여 100이하의 수 중에 짝수들만의 합계를 구하시오.

sum = 0

for i in range(1,101): # 1~100 의 숫자 범위
    if i%2 == 0: # 조건 1 숫자가 2로 나눴을 때 나머지가 0이면 = 짝수
        sum += i # i의 합계
print(sum)


# In[134]:


# range를 사용하여 100 이하의 수 중에 짝수들만의 합계를 구하시오.

# range(start, stop, step)

for i in range(11): # start를 생략하면 0에서 시작
    print(i)


# In[136]:


# range(start, stop, step)

for i in range(0,11,2): # stop 을 생략하면 1씩 증가, 즉 step에 2를 넣으면 짝수 증가
    print(i)


# In[141]:


# 리스트 축약/내포 List Comprehension, 파이썬에서만 사용(특징)
# 리스트를 좀 더 편리하고 직관적으로 만드는 방법

list1 = [1,2,3,4]

print(list1)

list2 = [num     for num in list1] # 리스트1에 있는 숫자를 하나씩 출력함.

print(list2)

list3 = [num*2   for num in list1] # 리스트1에 있는 숫자에 2를 곱해 출력함.

print(list3)

list4 = [num     for num in list1    if num % 2 == 0] # 리스트1에 있는 숫자 중 짝수만 출력함.

print(list4)


# In[146]:


no = 70

if no >= 70:
    print("합격입니다.")
else:
    print("불합격입니다.")
    
# if를 표현하는 또 다른 방법
# "True" if 조건 else "False"
print("합격입니다."     if no >= 80     else     "불합격입니다.")


# In[ ]:




