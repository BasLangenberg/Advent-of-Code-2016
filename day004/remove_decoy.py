from collections import OrderedDict
import re

def is_real(line):
    validation = re.findall(r'\[(.*?)\]',line[-1])
    encrypted_string = ''
    linecount = 0
    while linecount < line.__len__() - 1:
        encrypted_string += line[linecount]
        linecount += 1

    all_words = list({(char, encrypted_string.count(char)) for char in encrypted_string})
    all_words.sort(key=lambda x: (-x[1], x[0]))

    calculated_checksum = "".join([byte for byte, count in all_words])

    if calculated_checksum[:5] == str(validation[0]):
        # return int(line[-1].strip('['))
        return int(str(line[-1]).split('[')[0])
    else:
        return 0

# 5342
# 375110
# 139587
# 245102

if __name__ == '__main__':

    real = []
    count_total = 0

    with open('input_data_part_one.txt', 'r') as file:
        for line in file:
            line = line.strip('\n')
            data = line.split('-')
            count_total += is_real(data)

    print(count_total)

