from tkinter import N


def is_palindrome_str(value: str) -> bool:
    '''Checks if a string is a palindrome. Get reversed string and check if equal to forward string.'''
    return value == value[::-1]  # reverse


def is_palindrome_int(n: int) -> bool:
    '''Checks if an int is a palindrome. Get the reversed int and check if equal to forward int.'''
    forward = n
    reversed = 0
    while 0 < n:
        lowest_digit = n % 10
        reversed = reversed * 10 + lowest_digit
        n = n // 10  # shift digits with floor division
    return forward == reversed


def is_palindrome(value) -> bool:
    '''Checks whether something is a palindrome or not. Only works with str or int.'''
    if isinstance(value, str):
        return is_palindrome_str(value)
    elif isinstance(value, int):
        return is_palindrome_int(value)
    else:
        raise TypeError(
            f'\'{value=}\' is {type(value)}. is_palindrom only works for for str or int.'
        )


def main():
    print(f'{is_palindrome("121")=}')
    print(f'{is_palindrome("1231")=}')
    print(f'{is_palindrome(121)=}')
    print(f'{is_palindrome(1231)=}')
    try:
        f'{is_palindrome(["121", "1231"])}'
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()