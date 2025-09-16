import time
from functools import cache


@cache  # 无限制缓存
def fib(n: int) -> int:
    """返回第 n 个斐波那契数"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start = time.time()
    print("fib(35) =", fib(35))
    print("第一次耗时:", round(time.time() - start, 6), "秒")

    start = time.time()
    print("fib(35) =", fib(35))  # 直接命中缓存
    print("第二次耗时:", round(time.time() - start, 6), "秒")
