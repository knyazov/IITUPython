def test_prime(n):
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
    print(f"test_prime({n}) = {isPrime}")


n = int(input())
test_prime(n)
