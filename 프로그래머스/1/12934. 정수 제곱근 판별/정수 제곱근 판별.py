def solution(sqrt):
    n = sqrt ** (0.5)
    if n % 1 == 0:
        return (n+1) ** 2
    return -1