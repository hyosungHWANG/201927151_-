#예제2, 변수의 타입에 주의
a = input("당신의 나이는?")
#위에서 변수형태를 바꿀 경우 type은 int가 된다.
#밑에 print에서 바꿀 경우 type은 str이다.

print(a, "살 이군요")
print("내년엔", int(a)+1, "살이 되네요")
print(type(a))

#예제2-1
a = input("당신의 나이는?")
# a = int(input("당신의 나이는?")) 이와 같이 할 경우 31line에서 오류 발생, 문자와 숫자의 합이 된다.
#자료형에 항상 주의
msg = a + "살 이군요"

print(msg)
print("내년엔", int(a)+1, "살이 되네요")
print(type(a))

#예제3
a = "파이썬"
print(a, "아 반가워")

msg = a + '아 반가워'
print(msg)

print("%s아 반가워~"%a)