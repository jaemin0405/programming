'''
    작성일 : 2024년 4월 11일
    작성자 : 컴퓨터 공학과 202495017 정재민
    설명 : 반복문 while
        
    [문제분석]
       
      
    [알고리즘]
    
    
'''
#1~10까지 출력하기
print("====반복문 while로 1부터 10까지 출력하기.1 ====")
num1 = 1 #초기값 1부터
while num1 <= 10: #조건식. 숫자를 10까지
    print(num1, end= ',') #반복하면서 할 일.
    num1 = num1 + 1 #증감식. 숫자를 1씩 증가하면서
    #증감식은 항상 반복문의 제일 마지막에 작성.

print() #한 줄 바꿈

print("====반복문 while로 1부터 10까지 출력하기. 2 ====")
num1 = 1 # 초기 값
num2 = 10 # 종료 값
while num1 <= num2 :
    print(num1, end= ',') #반복하면서 할 일.
    num1 = num1 + 1 #증감식. 숫자를 1씩 증가하면서
    
print() #한 줄 바꿈

print("===반복문으로 자기 이름 10개 출력하기 ===")
#1. 정재민     2.정재민.... 10.정재민
i = 1
while i <= 10 :
    print(i, end='.  ')
    print("1. 정재민")
    i = i + 1


    