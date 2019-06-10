def get_message():
    """None -> list

    Get a binary message from the user's input.

    """
    while True:
        try: 
            n = input("Enter a binary message with the length of 4: ")
            s = set(n)
            check_set = {'0', '1'}
            if len(n) == 4 and check_set >= s:
                mes = [int(i) for i in n]
                return mes
            else:
                print("You entered the wrong value ", n)
        except ValueError:
            print("You entered the non-binary value")


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


def encrypt_message(matrix, message):
    """(list, message) -> list

    Encrypt message with Hamming (7,4) code

    """
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
    2
    >>> get_corrected_bit_from_message(9, [1,2,5,4])
    4
    """
    if n > len(message)+3:
        return message[-1]
    elif n < 4:
        return message[n-2]
    else:
        return message[n-3]


def convert_list_to_string(l):
    """(list) -> str

    Concatenates list l to str

    >>> convert_list_to_string([1, 2, 3])
    '123'
    >>> convert_list_to_string(['h','e', 'y', '!'])
    'hey!'
    """
    return ''.join(map(str, l))


def show_result(message, code):
    """(list, list)

    Print result of encrypting message in Hamming code in the appropriate way

    >>> show_result([1, 0, 1, 0], [1, 0, 1, 1, 0, 1, 0])
    Hamming (7,4) code for message 1010 is: 1011010
    """
    print("Hamming (7,4) code for message ", end='')
    print(convert_list_to_string(message), end='')
    print(" is:", convert_list_to_string(code))


if __name__ == "__main__":
    message = get_message()
    matrix = get_matrix()
    code = encrypt_message(matrix, message)
    show_result(message, code)
