def isPalindrome(number: int) -> bool:
    number = str(number)
    number_mirror = number[::-1]
    return number == number_mirror


print(isPalindrome(123431))
