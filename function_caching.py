# import functools
from functools import lru_cache
import time

# @functools.lru_cache(maxsize=None)
@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)

    return n*5

print(fx(20))
print("done for 20")

print(fx(2))
print("done for 2")

print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")

print(fx(2))
print("done for 2")

print(fx(6))
print("done for 6")

print(fx(77))
print("done for 77")