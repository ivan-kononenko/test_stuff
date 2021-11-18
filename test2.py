min_val = float("-inf")
max_val = float("inf")
for x in range (-40000, 10000):
    y = 3.1*x**3 + 10.3*x**2 -2.8*x + 10.3
    if y < max_val:
        min_val = y
    if y > min_val:
        max_val = y

print(min_val, max_val)
