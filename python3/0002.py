# Problem 2: Find the sum of even numbers in Fibonacci sequence
# using terms not exceeding 4 million.


def fib_add_even():
    sum_even, prev_num, num = 0, 0, 1
    while sum_even < 4000000:
        new_num = prev_num + num
        prev_num = num
        num = new_num
        if new_num % 2 == 0:
            sum_even += new_num
    return sum_even


print(fib_add_even())
