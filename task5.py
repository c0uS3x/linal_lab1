from typing import Dict, List, Tuple
from sympy import totient, factorint
from math import prod

def fact(n: int) -> int:
    """Вычисляет n! простым циклом."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def factors_of(num: int) -> Dict[int, int]:
    """Разложение числа на простые множители (p: степень)."""
    return factorint(num)


def factorial_plus_one_data() -> Dict[int, Dict[int, int]]:
    """
    Для n = 2..50 вычисляет разложения n! + 1.
    Выводит:
      • максимум количества различных простых делителей,
      • случаи с 'большим' простым (> 10^6).
    Возвращает словарь {n: {p: exp, ...}}.
    """
    results: Dict[int, Dict[int, int]] = {}
    most_diverse: Tuple[int, int] = (0, 0)  # (n, count)
    big_threshold = 10**6
    large_primes: List[Tuple[int, int]] = []

    for n in range(2, 51):
        value = fact(n) + 1
        fct = factors_of(value)
        results[n] = fct

        count = len(fct)
        if count > most_diverse[1]:
            most_diverse = (n, count)

        for p in fct:
            if p > big_threshold:
                large_primes.append((n, p))

    print(f"Больше всего различных простых множителей при n = {most_diverse[0]} → {most_diverse[1]} шт.")
    if large_primes:
        print("Случаи с большими простыми (>10⁶):")
        for n, p in large_primes:
            print(f"  n = {n}, множитель {p}")

    return results
