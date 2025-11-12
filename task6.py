import time
from typing import List
from math import gcd, isqrt
from sympy import totient, factorint


def euler_phi_direct(n: int) -> int:
    """Вычисляет (n) прямым перебором."""
    if n == 1:
        return 1
    cnt = 0
    for k in range(1, n + 1):
        if gcd(k, n) == 1:
            cnt += 1
    return cnt

def euler_phi_factor(n: int) -> int:
    # Вычисляем φ(n) через разложение на простые множители
    if n <= 0:
        return 0
    factors = factorint(n)  
    result = n
    for p in factors:
        result = result // p * (p - 1)
    return result


def compare_euler_phi_methods(test_values: List[int]) -> Dict[str, List[float]]:
    results = {"direct": [], "factor": [], "sympy": []}

    for num in test_values:
        # прямой метод
        start = time.perf_counter()
        euler_phi_direct(num)
        results["direct"].append(time.perf_counter() - start)

        # факторизация
        start = time.perf_counter()
        euler_phi_factor(num)
        results["factor"].append(time.perf_counter() - start)

        # библиотечный (sympy)
        start = time.perf_counter()
        totient(num)
        results["sympy"].append(time.perf_counter() - start)

    return results