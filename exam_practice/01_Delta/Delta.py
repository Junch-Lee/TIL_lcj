import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# 1. 상하좌우의 델타값 사전 지정
dr = [-1, 1, 0, 0]
dc = [ 0, 0, -1, 1]


for tc in range(1, T+1):

    N = int(input()) # NxN 행렬의 길이 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # NxN 행렬 입력
    total = 0 # 최대값의 초기값

    for r in range(N):     # 2. 전체 행 -> 열 순으로 순회
        for c in range(N):
            
            for d in range(4): # 3. 기준점의 이웃한 요소들에 대해
                nr = r + dr[d] # 좌표값 계산
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < N: # 4. 유효한 범위 내에서

                    minus = arr[nr][nc] - arr[r][c] # 차이값 계산
                    if minus < 0: # 만약 차이값이 음수일 경우
                        minus = arr[r][c] - arr[nr][nc] # 두 수의 위치를 바꿔서 계산
                    
                    total += minus # 차의 절대값을 모두 합산

    print(f"#{tc} {total}")