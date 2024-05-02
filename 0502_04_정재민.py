'''
    작성일 : 2024 05 02
    작성자 : 정재민
    설명 : 커피자판기
    
    
    [문제분석] 
    0을 입력하기 전까지는 주문을 할 수 있다.
    1. 아메리카노를 선택하면 수량을 입력할 수 있다,.
    아메리카노 1500원 * 수량 계산
    각 메뉴에 대한 총 가격을 계산
    
    계속 메뉴를 선택할 수 있다
    0을 입력하면
    총 금액을 알려준다
    지불할 금액을 입력 받아 거스름돈을 알려준다.
    
    [알고리즘]
        1. 메뉴 보여주기
        2. 총 금액 변수 초기화
        3. 계속 반복하면서
            3-1. 주문할 음료 번호를 입력 받는다
            3-2. 0이 입력되면
                3-2-1. 주문을 종료한다 break
            3-3. 아니면
                3-3-1. 주문할 잔 수를 입력 받는다.
                3-3-2. 만약 1번이 아메리카노이면
                    3-3-2-1. 총금액 = 1500 *  잔 수 계산
                3-3-3. 아니고 만약 2번 카페라떼이면
                    3-3-3-1 총금액 = 2500 * 잔수
                3-3-4. 아니고 만약 3번 레몬에이드이묜
                    3-3-4-1. 총 금액 = 2000 * 잔수 
        4. 만약에 총 금액이 0이면
            4-1. 감사합니다
        5.아니면
        5-1. 총 금액 출력
        5-2 지불할 금액 입력 받기
        5-3 거스름돈 계산
        5-4. 가스름돈 알려준다 출력
                     
'''

while True :
    print("주문을 시작합니다.")
    print("1. 아이스 아메리카노 - 1,500원")
    print("2. 카페 라떼 - 2,500원")
    print("3. 레몬 에이드 - 2,000원")
    print("1. 아이스 아메리카노 - 1500원")
    print("0. 주문 종료")
    
    total_price = 0
while True :
    choice = int(input("주문할 음료의 번호를 입력하세요. (0입력시 주문)"))
    if choice == 0 :
        break
    elif choice < 0 or choice > 3:
        print("올바른 번호를 입력하세요.")
        continue
    else: 
        cup = int(input("주문할 잔 수를 입력하세요."))
        if choice == 1:
            total_price += 1500 == * cup
        elif choice ==2 :
            total_price += 2500 == * cup
        elif choice ==2 :
            total_price += 2000 == * cup

    
    if total_price == 0:
        print("주문이 종료 되었습니다.")
    break

    print("총 주문 금액은 {} 입니다.".format(total_pritce))
    
    while True :
        pay = int(input("지불할 금액을 입력하세요"))
    if pay < total_price:
        print("금액이 부족 다시 입력")      
    else :
        change = pay - total_price
        print("거스름돈은 {}입니다.".format(total_price)) 
