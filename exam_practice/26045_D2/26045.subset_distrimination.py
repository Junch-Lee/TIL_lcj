import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())

def is_subset(t, p, N, M):

    # 1. B의 각 요소를 가져옴 i
    # 2. A의 첫번째 부터 순회 j 
    # 3. 일치하는 값이 존재 -> j = j + 1부터, i + 1
    # 4. j가 살펴볼 범위 -> 일치하는 값 존재 시마다 1칸씩 뒤로 미뤄야함 (M - N + 1 + i)
    i = 0
    j = 0
    subset = False
    count = 0

    while i < M and j < N: 

        if p[i] == t[j]: # 일치하면
            i += 1 # pattern의 다음 글자 탐색
            j += 1 # target의 다음 글자 탐색
            count += 1 # 카운트 증가 

        else: # 불일치하면 
            j += 1 # target의 다음 글자를 탐색, pattern의 경우는 일치할 시에만 이동
        
        if count == M:
            subset = True
            break

    return subset

for tc in range(1, T+1):

    N, M = map(int,input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if is_subset(A, B, N, M):
        print(f"#{tc} YES")

    else:
        print(f"#{tc} NO")