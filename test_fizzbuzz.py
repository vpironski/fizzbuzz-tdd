import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("n, expected", [
	(3, "Fizz"),
	(6, "Fizz"),
	(5, "Buzz"),
	(10, "Buzz"),
	(15, "FizzBuzz"),
	(30, "FizzBuzz"),
	(1, 1),
	(2, 2),
	(7, 7)
])
def test_fizzbuzz(n, expected):
	assert fizzbuzz(n) == expected
