def add(first, second, n = 10):
    added_val = first + second
    added_val = convert_base(added_val, n)
    return added_val

def fibonacci(length):
    def internal(first, second, count):
        third = add(int(first), int(second))
        count -= 1
        if count == 1: #originally 0
            return int(third)
        else:
            return internal(second, third, count)

    return internal(0, 1, length)

HEX_CHARS = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(num, n):
    """Change a base 10 number to a base-n number. Supports up to base 16. """
    new_num_string = ''
    current = num
    while current != 0:
        remainder = current % n
        if remainder > 9:
            remainder_string = HEX_CHARS[remainder]
        elif remainder >= 36:
            remainder_string = '('+str(remainder)+')'
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string+new_num_string
        current = current//n
    return new_num_string

def factorial(num):
    for i in range(num, 0):
        num = num*i
        return num
