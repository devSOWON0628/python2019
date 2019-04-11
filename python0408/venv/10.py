year=int(input("연도를 입력하시오"))

if ((year%4==0)and(year%100!=0))or(year%400==0):
    print("연도가 4로 나누어 떨어지면 윤년이다.")