#Filter even numbers, map to their squares, reduce to sum
from functools import reduce
print(reduce(lambda acc, x: acc + x, map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, 11)))))


#Filter strings containing "a", map to uppercase, reduce to concatenate
from functools import reduce
print(reduce(lambda acc, x: acc + x, map(str.upper, filter(lambda s: 'a' in s, ["apple", "banana", "cherry", "date"]))))


#Filter odd numbers, map to cubes, reduce to list of strings
from functools import reduce
print(reduce(lambda acc, x: acc + [x], map(lambda x: str(x**3), filter(lambda x: x % 2 == 1, range(1, 10))), []))


# Filter words longer than 3 letters, map to lengths, reduce to total length
from functools import reduce
print(reduce(lambda acc, x: acc + x, map(len, filter(lambda w: len(w) > 3, ["cat", "elephant", "dog", "rabbit"]))))

#Filter prime numbers, map to strings, reduce to joined string
from functools import reduce
print(reduce(lambda acc, x: acc + " " + x, map(str, filter(lambda n: all(n % i != 0 for i in range(2, int(n**0.5) + 1)), range(2, 20)))))

#Filter multiples of 3, map to their doubles, reduce to sum
from functools import reduce
print(reduce(lambda acc, x: acc + x, map(lambda x: x * 2, filter(lambda x: x % 3 == 0, range(1, 11)))))

#Filter numbers divisible by 5, map to strings, reduce to a single string
from functools import reduce
print(reduce(lambda acc, x: acc + x, map(str, filter(lambda x: x % 5 == 0, range(1, 51)))))

#Filter vowels, map to uppercase, reduce to a single string
from functools import reduce
print(reduce(lambda acc, x: acc + x, map(str.upper, filter(lambda c: c in "aeiou", "abcdefghij"))))

# Filter pairs with even sums, map to their sums, reduce to product
from functools import reduce
print(reduce(lambda acc, x: acc * x, map(sum, filter(lambda pair: sum(pair) % 2 == 0, [(i, j) for i in range(1, 4) for j in range(1, 4)]))))

#Filter negative numbers, map to their absolute, reduce to max
from functools import reduce
print(reduce(lambda acc, x: acc if acc > x else x, map(abs, filter(lambda x: x < 0, [-1, -2, -3, 4, 5]))))

