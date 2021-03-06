import itertools


def get_prime(N):
    prime = [True] * (N + 1)
    for i in range(2, int(N ** 0.5)):
        if prime[i]:
            for j in range(i + i, N + 1, i):
                prime[j] = False
    return prime


def solution(numbers):
    answer = 0
    prime = get_prime(10000000)

    permu = []
    for i in range(1, len(numbers) + 1):
        permu += list(map(''.join, itertools.permutations(numbers, i)))
    permu = list(map(int, permu))

    for p in set(permu):
        if prime[int(p)] and int(p) > 1:
            answer += 1

    return answer