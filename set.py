one_digit_numbers={0,1,2,3,4,5,6,7,8,9}
numbers_after_eight = {9,10,11,12,13}
print(one_digit_numbers.intersection(numbers_after_eight))
print(one_digit_numbers.union(numbers_after_eight))
print(one_digit_numbers.difference(numbers_after_eight))
print(numbers_after_eight.difference(one_digit_numbers))
