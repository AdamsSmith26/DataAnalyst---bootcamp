def evaluate(a, x, b, c):
    return a*x*x+b*x+c

a, x, b, c = map(int, input().split())

res = evaluate(a, x, b, c)
print(res)