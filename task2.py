from typing import List

def palindromic_cubes_and_palindromic_primes() -> tuple[List[int], List[int]]:
    """
    Возвращает:
    tuple:
    - список всех палиндромов a < 100000, для которых a^3 — палиндром;
    - список всех простых p <= 10000, которые являются палиндромами.
    """
    palindromic_squares = [int(a) for a in range(10**5) if is_palindrom(a) and is_palindrom(a**3)]
    circular_primes = []
    for p in range(2, 10**4 + 1):
        if is_prime(p) and is_palindrom(p):
            circular_primes.append(p)
    return palindromic_squares, circular_primes