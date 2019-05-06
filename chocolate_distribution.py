def distribute_chocolates(n, ratings):
    distribution = [1] * n
    for i in range(1, len(ratings) - 1):
        rating = ratings[i]
        left_rating = ratings[i - 1]
        right_rating = ratings[i + 1]
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
