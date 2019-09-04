def chocolates(n, arr):
    if n <= 0 or n >= 100000:
        return -1
    for i in arr:
        if i <= 0 or i >= 100000:
            return -1
    distribution = [1] * n
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1]:
            if distribution[i] <= distribution[i - 1]:
                distribution[i] = distribution[i - 1] + 1
        if arr[i] > arr[i + 1]:
            if distribution[i] <= distribution[i + 1]:
                distribution[i] = distribution[i + 1] + 1
    return sum(distribution)


def distribute_chocolates(n, arr):
    distribution = [1] * n
    for i in range(1, len(arr) - 1):
        rating = arr[i]
        left_rating = arr[i - 1]
        right_rating = arr[i + 1]
        if rating > left_rating:
            if distribution[i] <= distribution[i - 1]:
                distribution[i] = distribution[i - 1] + 1
        if rating > right_rating:
            if distribution[i] <= distribution[i + 1]:
                distribution[i] = distribution[i + 1] + 1
    return sum(distribution)


if __name__ == '__main__':
    n = int(input())
    ratings = []
    for i in range(0, n):
        ratings.append(int(input()))
    print(distribute_chocolates(n, ratings))
