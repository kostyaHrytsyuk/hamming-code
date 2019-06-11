import ham_code
import string_processor

if __name__ == "__main__":
    message = string_processor.get_message()
    code = ham_code.encrypt_message(message)
    string_processor.show_result(message, code)
