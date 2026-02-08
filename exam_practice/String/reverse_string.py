import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 문자열을 다룰 때 핵심? 
# 문자열도 시퀀스다 라는 점. 인덱스를 통해 접근해줄 수 있다는 것을 잊지말자 
# 회문에서와 마찬가지로 중요한 부분
# 어느 부분까지 특정 동작을 수행해줄 것인가? 의 문제점

# 1. 본 문자열을 그대로 뒤집는 방법 

def reverse_string(list1):

    N = len(list1) 

    for idx in range(N//2):
        list1[idx], list1[N-1-idx] = list1[N-1-idx], list1[idx]

    temp = "".join(list1)
    return temp

# 2. 빈 문자열을 지정해 뒤에서부터 넣어주는 방법

def reverse_string2(word):

    N = len(word)
    reversed_string = "" # 뒤에서부터 넣어줄 빈 문자열 

    for idx in range(N-1, -1, -1):
        reversed_string += word[idx]

    # for idx in range(N):
    #   reversed_string += word[N-1-idx]

    return reversed_string

def reverse_string3(word):

    N = len(word)
    result = ""

    for char in word:
        result = char + result

    return result

for tc in range(1, 2):

    # str_list = list(input().strip())

    # reversed_str = reverse_string(str_list)

    # print(reversed_str)
    word = input()

    reversed_str2 = reverse_string2(word)

    reversed_str3 = reverse_string3(word)

    print(reversed_str2)
    print(reversed_str3)



