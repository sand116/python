def positive(numberList) :
    return numberList > 0
# 일반적으로 리스트로 비교연산자 사용 불가능
# filter(함수, iterable args) - 리턴 값이 참인 것만 묶어서 돌려줌
print(list(filter(positive,[3,2,1])))

# 람다 사용 lambda 인자 : return값 - 리스트 내에서도 사용 가능
print(list(filter(lambda x: x>0,[1,-3,2,0])))
