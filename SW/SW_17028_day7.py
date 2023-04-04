'''
사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때
가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 함

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때
최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오
'''

T = int(input())

for tc in range(T):
    v,e = map(int,input())