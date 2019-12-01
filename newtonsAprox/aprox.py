# Numerical Root Aproximator
# Given x, n \in R, calculate x^(1/n)

def newton_integer(x, n, r0=1, delta=10**-15):
    # Assumes that n is an integer
    ri = r0

    r_new = ri - (ri**n - x)/(n * ri**(n - 1))
    while (abs(r_new - ri) > delta):
        ri = r_new
        r_new = ri - (ri**n - x)/(n * ri**(n - 1))
    return r_new


# Test: Find the square root of 4. i.e. newton(4, 2)
print('newton(4, 2):', newton_integer(4, 2))
print('newton(5, 2):', newton_integer(5, 2))

def newton(x, n, r0=1, delta=10**-4):
    #General Newton root aproximator
    # 1/n ~= b/a ->
    # x^(1/n) ~=  x^(b/a) = (x^(1/a))^b
    # Let x' = x^(1/a), then  x^(b/a) = x'^b = newton(x, a)**b

    # Find a, b s.t. n ~= a/b
    
    a = int((n * (10**4) * 10 - .5))/10.0
    b = 10**4

    return newton_integer(x, a)**b

x = 1024
n = 2

print(str(x) + '^(1/' + str(n) + ') = ' + str(newton_integer(x, n)))

