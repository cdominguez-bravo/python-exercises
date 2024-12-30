# integersums.py
def first(n):
    num = 1
    sum = 0
    while num < n + 1:
        sum = sum + num
        num = num + 1
    return sum

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"The sum of the first {n} integers is: {first(n)}")
    else:
        print("Usage: python integersums.py <number>")