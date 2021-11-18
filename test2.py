C = [[3.1, 10.3, -2.8, 10.3], [2.1, 8.8, -11.4, -5.6], [1.6, 0.2, -20.8, 38.5]]    
for i in range(0, 3):
    min_val = float("inf")
    max_val = float("-inf")
    for x in range (-40000, 10000):
        x = x/10000
        y = C[i][0]*x**3 + C[i][1]*x**2 + C[i][2]*x + C[i][3]
        if y > max_val:
            max_val = y
        if y < min_val:
            min_val = y

    print(f"Min: {min_val:.4f}, Max{max_val:.4f}")
