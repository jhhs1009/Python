'''
백준 1541 - 잃어버린 괄호 [그리디]

세준이는 양수와 +,-,괄호를 가지고 식을 만들었다.

그리고 세준이는 괄호를 모두 지웠다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

풀이 )

괄호를 적절하게 사용...그리디

연산자의 갯수에 따른 결과 값

-> 이런문제
: 식의 결과를 최소로 만드는 것이 목적이라는 걸 명심
: 최초로 마이너스가 나오기 전까지 나오는 숫자는 모두 더할 수 밖에 없으며,
: 이후 마이너스가 나오는 순간 그 뒤에 있는 모든 수들을 빼주면 된다.

'''

s = list(input())

print(s)