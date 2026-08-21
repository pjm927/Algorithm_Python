# 1부터 10까지의 두 수를 골라 합이 10이 되는 경우 찾기

# 방법 1: 모든 조합을 확인하는 완전탐색
for i in range(1, 11):
    for j in range(1, 11):
        if i + j == 10:
            print(i, j)

print('-' * 30)

# 방법 2: i가 정해지면 j = 10 - i임을 이용
for i in range(1, 10):
    j = 10 - i
    print(i, j)