def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

p = 6184582007
q = 49472019391
r = 1234567

n = p*q
m = (p-1)*(q-1)
print m

print gcd(m, r)


rprime = 92997030944953466880

210831866869623840412


236621645496453797068, 41864260073650084250.
