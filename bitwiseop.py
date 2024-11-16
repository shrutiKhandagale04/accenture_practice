def operations_binary_string(s):
    if s is None:
        return -1

    # Start with the first binary digit as the initial result
    result = int(s[0])
    i = 1

    while i < len(s) - 1:
        operator = s[i]
        next_digit = int(s[i + 1])
        
        if operator == 'A':
            result &= next_digit  # AND operation
        elif operator == 'B':
            result |= next_digit  # OR operation
        elif operator == 'C':
            result ^= next_digit  # XOR operation
        else:
            return -1  # Invalid operator
        
        i += 2

    return result
print(operations_binary_string("1C0C1C1A0B1"))  # Output should be 1
