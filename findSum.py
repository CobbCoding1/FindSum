a = [1, 2, 3, 4]
b = [15, 30, 55, 120]

target = 16


def findSum(a, b, target):
    l = []
    for i in range(len(a)):
        l.append(a[i])
    for i in range(len(b)):
        result = l[i] + b[i]
        if result == target:
            return True
        return False


print(findSum(a, b, target))
