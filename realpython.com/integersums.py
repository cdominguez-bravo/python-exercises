# integersums.py
def first(n):
    num = 1
    sum = 0
    while num < n + 1:
        sum = sum + num
        num = num + 1
    return sum

# integersums.py
def better(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum