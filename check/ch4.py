import base
import ch2
from ch3_0 import EXPECTED, NOT_EXPECTED


EXPECTED += [
    "Test 04_1 OK51135!",
    "Test 04_4 test OK51135!",
    "Test 04_5 ummap OK51135!",
    "Test 04_6 ummap2 OK51135!",
]

NOT_EXPECTED += [
    "Should cause error, Test 04_2 fail!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
