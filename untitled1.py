import sys
n = input("Enter the number:")
if not n.isdecimal():
    print("n is not decimal")
    sys.exit(0)
n = int(n)
a = [True] * (n+1)
for i in range(2, n):
    if a[i] == True:
        for j in range(i**2, n, i):
            a[j] = False
primes = []
for i in range(2, n+1):
    if a[i] == True:
        primes.append(i)
print("Primes ", primes)
f = open("primes.txt", 'w')
primes = str(primes)
f.write(primes)
f.close()
