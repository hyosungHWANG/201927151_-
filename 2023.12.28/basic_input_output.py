#program 2-1
print('부산대학교')
print('기초교육원')
print('컴퓨팅적 사고와 코딩')

#program 2-2,4,5
#화면에 여러 줄을
#출력하는 방법에 대한 코드입니다.
print("부산대학교") #첫 번째 줄에 '부산대학교'를 출력합니다.
print("기초교육원") #두 번째 줄에 '기초교육원'을 출력합니다.
print("컴퓨팅적 사고와 코딩")   #세 번째 줄에 '파이썬 프로그래밍 기초'를 출력합니다.

#program 2-3
print("""One
Two
Three""")

#program 2-6,7
#하나의 변수를 활용하는 코드입니다.
Lab = 105
print('우리가 수업하는 실습실:')
print(Lab)
print('우리가 수업하는 실습실:',Lab)

#program 2-8
#변수 두 개를 생성하고 값을 할당
my_id = 201927151
grade = 3

#두 개의 변수에 할당된 값을 출력
print('나의 학번:')
print(my_id)
print('학년:')
print(grade)

#program 2-9
#변수에 값을 할당하고 출력하는 예제입니다.
#dollars 변수에 값을 할당해봅시다.
dollars = 2.75
print('I have', dollars, 'in my account')

#dollars 변수에 새로운 값을 할당해봅시다.
dollars = 99.95
print('But now I have', dollars, 'in my account')

#program 2-10
#두 개의 변수를 생성하고 문자열을 할당합니다.
department = '항공우주공학과'
name = '황효성'

#각 변수에 할당된 문자열 값을 출력해보자
print(department, name)

#program 2-11
#학과명을 입력받습니다.
department = input('학과명:')

#여러분의 이름을 입력받습니다.
name = input('성명: ')

#두 변수의 값을 출력합니다.
print('안녕하세요', department, name)

#program 2-12
#여러분의 이름, 나이, 통학시간 정보를 입력받습니다.
name = input('당신의 이름은 무엇입니까? ')
age = int(input('나이는 어떻게 되시나요? '))
attending_time = float(input('통학시간은 얼마나 걸립니까? '))

#변수에 입력된 데이터를 출력해봅시다.
print('입력 정보는 다음과 같습니다.')
print('이름:', name)
print('나이', age)
print('통학시간', attending_time)

#program 2-13
#salary 변수에 급여를 할당합니다.
salary = 2500.0

#bouns 변수에 보너스를 할당합니다.
bouns = 1200.0

#급여와 보너스를 더하여 총 급여를 구해봅니다.
#총 급여를 pay 변수에 할당합니다.
pay = salary + bouns

#총 급여를 출력합니다.
print('총 급여: ', pay)

#program 2-14
#본 예제에서는 원가에 할인율을 적용하여 할인가격을 계산해보자.

#original price 변수에 원가를 입력받는다.
original_price = float(input("제품의 원가를 입력해주세요: "))

#원가에 할인율 20%를 적용하여 할인가를 계산하여 discount 변수에 할당한다.
discount = original_price*0.2

#원가에 할인가가 적용된 제품 가격을 계산하여 sale_price 변수에 할당한다.
sale_price = original_price - discount

#할인가가 적용된 제품 가격을 출력한다.
print('할인가격: ', sale_price)

#program 2-15
#세 과목의 평가 점수를 입력받고
#test1, test2, test3 변수에 각각 할당한다.
test1 = float(input('첫 번째 과목 점수를 입력해주세요: '))
test2 = float(input('두 번째 과목 점수를 입력해주세요: '))
test3 = float(input('세 번째 과목 점수를 입력해주세요: '))

#각 과목의 점수 평균을 계산하고
#그 결과 값을 average 변수에 할당한다.
average = (test1 + test2 + test3) / 3.0

#점수 평균을 출력한다.
print('3 과목의 평균 점수: ', average)

#program 2-16
#본 예제는 초를 입력받아 시, 분, 초로 변환하는 프로그램이다.
#초 값을 입력받아 total_seconds 변수에 할당한다.
total_seconds = float(input('시간 값을 초 단위로 입력해주세요: '))

#시간을 계산하여 hours 변수에 할당한다.
hours = total_seconds // 3600

#분을 계산하여 minutes 변수에 할당한다.
minutes = (total_seconds // 60) % 60

#초의 나머지 값을 seconds 변수에 할당한다.
seconds = total_seconds % 60

#시, 분, 초 값을 출력한다.
print('시 분 초는 다음과 같습니다.')
print('시: ', hours)
print('분: ', minutes)
print('초: ', seconds)

#program 2-17

# 본 예제는 목표액을 특정 이율로 얻고자 할 경우 매년 적립해야할 금액을 계산해보자. 
# 목표액을 입력받고 future_value 변수에 할당한다. 
future_value = float(input('목표 금액을 입력해주세요: '))

# 연간 이율을 입력받고 rate 변수에 할당한다. 
rate = float(input('연간 이율을 입력해주세요: '))

# 적립 기간을 입력받고 years 변수에 할당한다. 
years = int(input('저축 기간을 연 단위로 입력해주세요: '))

# 특정 기간동안 적립해야할 금액을 계산하여 present_value 변수에 할당한다. 
present_value = future_value / (1.0 + rate)**years

# 적립 금액을 출력한다. 
print('적립 금액: ', present_value)

#program 2-18

# print() 함수에서 쉼표로 데이터를 구분하여 출력할 때
# 자동적으로 분리되는 빈 칸을 sep 옵션으로 제어할 수 있다. 
print('a','b','c')
print('a','b','c',sep='')
print('a','b','c',sep='***')


#program 2-19

# print() 함수를 여러 번 사용할 경우, 각 print() 함수가 수행된 후에는
# 자동적으로 줄바꿈이 일어난다. 이는 커서가 자동으로 내려가기 때문인데
# 커서를 줄바꿈시키지 않고 바로 옆에 놓고 같은 줄에 여러 print() 함수의 내용을
# 나타내고자 할 때 end 옵션을 사용할 수 있다. 

print('a')
print('b')
print('c', end='')
print('d', end='')
print('e', end='***')
print('f')

#program 2-20

# 본 예제는 부동 소수점이 출력되는 연산을 수행해본다. 
# 소수점 길이를 제어하지 않고 결과 값을 출력한다. 
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print('월급여: ', monthly_payment)

#program 2-21

# 본 예제에서는 소수점 자리를 제어하여 결과를 출력해보자. 
amount_due = 5000.0
monthly_payment = amount_due / 12
print('월급여: ', format(monthly_payment, '.2f'))

#program 2-22
# 본 예제도 소수점 자리를 제어하여 결과를 출력해보자. 
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', format(annual_pay, ',.2f'), sep='')

#program 2-23

# 본 예제는 부동 소수점을 특정 너비에 맞추어 출력하는 방법에 대해 알아보자. 
# 아래와 같이 각 변수에 부동 소수점이 포함된 값을 할당한다. 
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# 7칸에 맞추어 부동 소수점이 포함된 변수 값을 출력한다. 
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))