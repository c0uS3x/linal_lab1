from typing import List, Dict, Tuple 

def is_palindrom(x: int) -> bool:
    return x == x[::-1]

def is_prime(x: int) -> bool:
    if x>1 and all([int(x) % i == 0 for i in range(2,int(x**0.5)+1)]):
        return True
    return False

def circular_permutations(s: str) -> List[str]:
    return [s[i:] + s[:i] for i in range(len(s))]

def palindromic_squares_and_circular_primes() -> tuple[List[int], List[int]]:
    """
    Возвращает:
    tuple:
    - список всех палиндромов a < 100000, для которых a^2 — палиндром;
    - список всех простых p < 1000000, все циклические перестановки цифр которых
    →
    просты.
    """
    palindromic_squares = [int(a) for a in range(10**5) if is_palindrom(a) and is_palindrom(a**2)]
    circular_primes = []
    for p in range(2, 10**6):
        if is_prime(p):
            if all([is_prime(int(rot)) for rot in circular_permutations(str(p))]):
                circular_primes.append(p)
    return palindromic_squares, circular_primes
