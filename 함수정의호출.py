#함수정의 한 후 반드시 함수 호출
#더하기 함수 정의
def add(a, b):
    c = a + b
    return c

#빼기 함수 정의
def minus(a, b):
    c = a - b
    return c

#곱하기 함수 정의
def multi(a, b):
    c = a * b
    return c

#나누기 함수 정의 
def divide(a, b):
    c = a / b
    return c

while True:
    a = input("1st input: ") 
    if a == "0000":
        break
    b = int(input("2nd input: "))
    a = int(a);
    
    result = add(a, b) #더하기 함수 호출
    print(a, "+", b, "=", result)
    result = minus(a, b) #빼기 함수 호출
    print(a, "-", b, "=", result)
    result = multi(a, b) #곱하기 함수 호출
    print(a, "*", b, "=", result)
    result = divide(a, b) #나누기 함수 호출
    print(a, "/", b, "=", result)
    
print("exit")
