# 학생 5명 중 2명을 뽑는 모든 조합 (순서 X, 중복 X)

for i in range(1, 6):
    # i보다 큰 번호부터 선택하여 중복 조합과 자기 자신 선택을 방지
    for j in range(i + 1, 6):
        print(i, j)