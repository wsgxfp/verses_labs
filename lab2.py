def find_sum(M, P):
    M.sort()
    N = len(M)

    for i in range(N - 2):
        left = i + 1
        right = N - 1
        while left < right:
            curr_sum = M[i] + M[left] + M[right]
            if curr_sum == P:
                return True
            elif curr_sum < P:
                if search_third(M, left, right, P - M[i] - M[left]):
                    return True
                else:
                    left += 1
            else:
                right -= 1
    return False


def search_third(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
P = 16

if find_sum(M, P):
    print("Такі числа є")
else:
    print("Таких чисел немає")
