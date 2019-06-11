import HamException


def get_message():
    """None -> list

    Get a binary message from the user's input.

    """
    while True:
        try:
            n = input("Enter a binary message with the length of 4: ")
            s = set(n)
            check_set = {'0', '1'}
            mes = []
            if len(n) == 4 and check_set >= s:
                for i in n:
                    if not str.isdigit(i):
                        raise HamException
                    else:
                        mes.append(int(i))
                return mes
            else:
                print("You entered the wrong value ", n)
        except HamException:
            print("You entered the non-binary value")


def convert_list_to_string(l):
    """(list) -> str

    Concatenates list l to str

    >>> convert_list_to_string([1, 2, 3])
    123
    >>> convert_list_to_string(['h','e', 'y', '!'])
    hey!
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
    print(" is: ", convert_list_to_string(code))
