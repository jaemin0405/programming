'''
    작성일 : 2024 05 02
    작성자 : 정재민
    설명 : 두 개의 정수를 입력받아
    첫 번째 정수가 두 번째 정수의 배수이면
    "00은 00의 배수이다. "를 출력하고,
    아니면 "00은 00의 배수가 아니다." 를 출력하는 프로그램을  작성하시오
    
    [문제분석] 
    배수는 나누어 나머지가 0인 수
    첫 번째 정수가 두 번째 정수의 배수이면
        => num1 % num2 ==0 :
        
        만약 두번째 수가 0이면 메세지를 출력한다
    
    [알고리즘]
        1. 두 정수를 입력 받는다.
        2. 만약 두번째 수가 0이면
            2-1. 0으로 나눌 수 없음을 출력한다.
        3. 아니면
            3-1. 만약 num1 % num2 == 0 :
            3-1-1. num1은 num2의 배수이다.
        3-2. 아니면
            3-2-1. num1 num2.의 배수가 아니다
            
'''

num1 = int(input("첫번째 정수 입력. :"))
num2 = int(input("두번째 정수 입력 :"))

if num2 == 0:
    print("0으로 나눌 수 없음")
else :
    
    if num1 % num2 == 0:
        print(f"{num1}은 {num2}의 배수이다")
    else :
        print(f"{num1}은 {num2}의 배수가아니다")
    
