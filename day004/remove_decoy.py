import re
#from pudb import set_trace; set_trace()

def is_real(line):
    is_real = True
    for segment in line:
        print(type(line))
        if '[' in segment:
            validation = re.findall(r'\[(.*?)\]',segment)
            for validator  in validation:
                for character in validator:
                    count = 0
                    segment_check = True
                    while count < line.__len__() - 2 and segment_check == True:
                        if character not in line[count]:
                            is_real = False
                        else:
                            segment_check = True
                        count += 1

    if is_real == True:
        return True
    else:
        return False

if __name__ == '__main__':

    real = []

    with open('input_data_part_one.txt', 'r') as file:
        for line in file:
            line = line.strip('\n')
            data = line.split('-')
            if is_real(data):
                real.append(line)

    print(real)
