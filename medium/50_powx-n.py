class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(b=x, exp=abs(n)):
            if exp == 0:
                return 1
            elif exp % 2 == 0:
                return func(b * b, exp // 2)
            else:
                return b * func(b * b, (exp - 1) // 2)
        f = func()
        return float(f) if n >= 0 else 1/f