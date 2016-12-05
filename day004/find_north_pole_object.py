UPPER_BOUND = ord('z')
LOWER_BOUND = ord('a')

def calculate_real_name(input_data):
    return_string = ' '

    # Get and remove number
    number = input_data.split('-')
    number = int(number[-1].split('[')[0])

    # Convert string to result
    for character in input_data:
        if character == '-':
            return_string += ' '
        else:
            code = ord(character)
            for num in range(number):
                code += 1
                if code > UPPER_BOUND:
                    code = LOWER_BOUND

            return_string += chr(code)

    # Return result
    return return_string

if __name__ == '__main__':
    # x = ord('a')
    # x += 1
    # print(chr(x))
    with open('input_data_part_one.txt', 'r') as file:
        for line in file:
            if calculate_real_name(line).__contains__('north'):
                print(line)

def test_translation():
    assert calculate_real_name('qzmt-zixmtkozy-ivhz-343') == 'very encrypted name'