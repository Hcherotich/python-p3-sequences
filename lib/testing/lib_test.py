#!/usr/bin/env python3

from sequences import print_fibonacci

import io
import sys


class TestPrintFibonacci:
    '''function print_fibonacci()'''
def print_fibonacci(length):
    if length == 0:
        print('[]')
        return

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)

    