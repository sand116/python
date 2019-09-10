'''
3. 깊은 복사(deep copy)
mutable 한 내부객체(내부리스트)의 문제를 해결하기 위해서는 얕은 복사가 아닌 깊은 복사(deep copy)를 해야 합니다.

얕은 복사가 복합객체(리스트)만 복사되고 그 안의 내용은 동일한 객체를 참조한다면, 깊은 복사의 경우에는 복합객체를 새롭게 생성하고 그 안의 내용까지 재귀적으로 새롭게 생성하게 됩니다.

그래서 깊은 복사를 하게 되면, 처음에 만들었던 객체와 복사된 객체가 전혀 달라지기 때문에 어느 한쪽을 수정한다고 해서 다른 한쪽이 영향 받는 일은 없게되겠죠.

파이썬에서는 copy 모듈의 deepcopy()라는 메서드를 통해 깊은 복사를 손쉽게 구현
'''

import copy

a = [1, [1, 2, 3]]
b = copy.deepcopy(a)    # deep copy 실행
print(b)    # [1, [1, 2, 3]] 출력
b[0] = 100
b[1].append(4)
print(b)    # [100, [1, 2, 3, 4]] 출력
print(a)    # [1, [1, 2, 3]] 출력

'''
1. 단순복제는 완전히 동일한 객체,
2. 얕은복사(shallow copy)는 복합객체(껍데기)만 복사, 그 내용은 동일한 객체
3. 깊은복사(deep copy)는 복합객체 복사 + 그 내용도 재귀적으로 복사
'''