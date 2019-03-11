def bu_fib(n):
    vals = [0, 1]
    for i in range(2, n+1):
        vals.append(vals[i-1] + vals[i-2])
    return vals[n]
