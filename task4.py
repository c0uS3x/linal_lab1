from typing import Dict, List

def primes_with_two_digits() -> Dict[str, List[int]]:
    """
    Возвращает словарь вида:
    {
    '13': [список первых 100 простых из {1,3}],
    '15': [список первых 100 простых из {1,5}],
    '17': [список первых 100 простых из {1,7}],
    '19': [список первых 100 простых из {1,9}]
    }
    """
    return {
    # '13': generate_primes('1', '3'),
    # '15': generate_primes('1', '5'),
    '17': generate_primes('1', '7'),
    # '19': generate_primes('1', '9')
    }


def generate_primes(d1: str, d2: str, limit: int = 100) -> List[int]:
    res = []
    length = 1

    while len(res) < limit:
        for num in range(10 ** (length - 1), 10 ** length):
            if all(ch in (d1, d2) for ch in str(num)):
                if is_prime(num):
                    res.append(num)
                    if len(res) == limit: 
                        break
        length += 1

    return res

#реже всего встречается набор (1,5) половина чисел оканчивается на 5 → делится на 5; из оставшейся половины ~1/3 делится на 3, остаётся малая доля кандидатов
#{1,9} 9 ≡ 0 (mod 3) — та же проблема с делимостью на 3
#{1,3} 3 ≡ 0 (mod 3), поэтому примерно 1/3 чисел имеет сумму цифр ≡ 0 (mod 3) → делимость на 3 и отбраковка
#{1,7} обе цифры ≡ 1 (mod 3), значит сумма цифр редко кратна 3, нет делимости на 3; нет чётных и цифры 5 — идеальный набор для простоты
