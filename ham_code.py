def get_matrix():
    """None -> list

    Build a generator matrix for the Hamming (7,4) code.

    """
    m = []
    for i in range(1, 8):
        a = list("{0:03b}".format(i))
        a.reverse()
        m.append([int(i) for i in a])
    return m


def encrypt_message(message):
    """(list, message) -> list

    Encrypt message with Hamming (7,4) code

    """
    matrix = get_matrix()
    code = []
    for i in range(len(matrix)):
        if (i & (i+1)) == 0:
            result = count_parity_bits(i, message, matrix)
            code.append(result)
        else:
            code.append(get_corrected_bit_from_message(i, message))
    return code


def count_parity_bits(n, message, matrix):
    """(int, list, list) -> int

    Count parity bits for Hamming (7,4) code

    """
    if n < 2:
        line_number = 2 ** n - 1
    else:
        line_number = n - 1
    bit = 0
    for i in range(len(matrix)):
        if i != n and matrix[i][line_number] == 1:
            corrected = get_corrected_bit_from_message(i, message)
            bit = bit ^ corrected
    return bit


def get_corrected_bit_from_message(n, message):
    """(int, list) -> int

    Returns value on corrected position from message for Hamming (7,4) code

    >>> get_corrected_bit_from_message(3, [1,2,5,4])
    5
    >>> get_corrected_bit_from_message(9, [1,2,5,4])
    4
    """
    if n > len(message)+3:
        return message[-1]
    elif n < 4:
        return message[n-2]
    else:
        return message[n-3]
