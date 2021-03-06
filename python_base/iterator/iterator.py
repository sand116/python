'''
이터레이터 - 숫잘르 하나씩 꺼낼 수 있는 객체 
지연 평가(lazy evaluation)
연속된 숫자를 미리 만들면 숫자가 적을 때는 상관없지만 숫자가 아주 많을 때는 메모리를 많이 사용하게 되므로 성능에도 불리합니다. 그래서 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을
때 값을 만드는 방식을 사용합니다. 즉, 데이터 생성을 뒤로 미훈

반복할 수 있는 객체 - 요소가 여러개 들어있고, 한번에 하나씩 꺼낼 수 있는 객체 __iter__ method가 들어있음

__iter__ 와 __next__  method를 이용하면 이터레이터를 만들 수 있음 

시퀀스 객체와 반복 가능한 객체의 차이
'Unit 11 시퀀스 자료형 활용하기'에서 리스트, 튜플, range, 문자열은 시퀀스 객체라고 했는데, 이 유닛에서는 반복 가능한 객체라고 했습니다. 시퀀스 객체와 반복 가능한 객체의 차이점은 무엇일까요?

다음 그림과 같이 반복 가능한 객체는 시퀀스 객체를 포함합니다.

리스트, 튜플, range, 문자열은 반복 가능한 객체이면서 시퀀스 객체입니다. 하지만, 딕셔너리와 세트는 반복 가능한 객체이지만 시퀀스 객체는 아닙니다. 왜냐하면 시퀀스 객체는 요소의 순서가 정해져 있고 연속적(sequence)으로 이어져 있어야 하는데, 딕셔너리와 세트는 요소(키)의 순서가 정해져 있지 않기 때문입니다. 따라서 시퀀스 객체가 반복 가능한 객체보다 좁은 개념입니다.

즉, 요소의 순서가 정해져 있고 연속적으로 이어져 있으면 시퀀스 객체, 요소의 순서와는 상관없이 요소를 한 번에 하나씩 꺼낼 수 있으면 반복 가능한 객체입니다.
'''
 
iter_object = [1, 2, 3].__iter__()
iter_object.__next__()