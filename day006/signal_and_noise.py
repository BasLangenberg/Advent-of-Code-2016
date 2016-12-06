def decrypt_column(input):
    width = input[0].__len__()
    hash = {}
    decrypt = ''
    for num in range(width):
        hash[num] = ''

    for string in input:
        for character in range(string.__len__()):
            hash[character] = hash[character] + string[character]

    for set in hash:
        count = 0
        winner = ''
        for char in hash[set]:
            if hash[set].count(char) > count:
                winner, count = char, hash[set].count(char)

        decrypt += winner

    return decrypt

def decrypt():
    input = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            input.append(line.strip('\n'))

    print(decrypt_column(input))

def test_decrypt():
    input = []
    with open('test_input.txt', 'r') as file:
        for line in file.readlines():
            input.append(line.strip('\n'))

    assert decrypt_column(input) == 'easter'

if __name__ == '__main__':
    decrypt()