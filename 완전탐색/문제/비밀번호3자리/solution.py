# 3자리 비밀번호의 모든 경우 생성
# 각 자리에는 0~9 사용 가능 (순서 O, 중복 O)

# 각 자리마다 0~9를 독립적으로 선택
for i in range(10):
    for j in range(10):
        for k in range(10):
            print(i, j, k)
