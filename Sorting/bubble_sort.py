def bubble_sort(arr):
    n = len(arr)

    # 한 번의 반복마다 가장 큰 값을 배열의 뒤쪽으로 이동
    for i in range(n - 1):
        for j in range(n - 1 - i):

            # 인접한 두 원소의 순서가 잘못되어 있으면 교환
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
