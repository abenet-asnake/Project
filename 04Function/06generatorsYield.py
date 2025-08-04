"""
======================================================================================================
Generators are special functions that lazily produce values one at a time using the yield keyword, 
making them ideal for memory-efficient processing of large datasets or infinite sequences.
=======================================================================================================

"""
 
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Key Characteristics
Lazy Evaluation: Values are generated on-demand

Memory Efficient: Only one value in memory at a time

Stateful: Remembers position between calls

Single Use: Can't rewind or reuse (unless recreated)

Uses yield (later in the code) to produce values one at a time, 
making it memory-efficient for infinite sequences.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

===================================================================================
Usage Scenarios
1. Large Datasets: Process large files or streams without loading everything into memory
2. Infinite Sequences: Generate sequences like Fibonacci or prime numbers on-the-fly
3. Iteration: Custom iteration logic without storing all values at once
4. data Pipelines: Stream data through multiple processing stages without intermediate storage

===================================================================================
"""

def fibonacci():
    """Generate infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Print first 10 Fibonacci numbers
fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 0 1 1 2 3 5 8 13 21 34

def prime_generator():
    """Generate infinite prime numbers"""
    # Helper function to check if a number is prime
    # we have two options the n value is  0 and 1
    # if n is less than 2, it is not prime  

    def is_prime(n):
        if n < 2:
            return False
        #it starts from 2, to stop n**0.5: Computes the square root of n
        #
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Print first 10 prime numbers
prime_gen = prime_generator()   
for _ in range(10):
    print(" Prime Number:",next(prime_gen))  # 2 3 5 7 11 13 17 19 23 29

