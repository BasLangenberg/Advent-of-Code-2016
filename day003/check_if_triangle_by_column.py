if __name__ == '__main__':

    count = 0
    column1 = []
    column2 = []
    column3 = []

    with open('input_day3.txt', 'r') as file:
        for line in file:
            collection = line.rstrip('\n').split(',')
            column1.append(int(collection[0]))
            column2.append(int(collection[1]))
            column3.append(int(collection[2]))

    # 1734 items per list == 578 iterations
    column1_count = 0
    column2_count = 0
    column3_count = 0

    while column1_count + 2 < column1.__len__():
        if column1[column1_count] + column1[column1_count + 1] > column1[column1_count + 2]:
            if column1[column1_count + 1] + column1[column1_count + 2] > column1[column1_count]:
                if column1[column1_count + 2] + column1[column1_count] > column1[column1_count + 1]:
                    count += 1

        column1_count += 3

    while column2_count + 2 < column2.__len__():
        if column2[column2_count] + column2[column2_count + 1] > column2[column2_count + 2]:
            if column2[column2_count + 1] + column2[column2_count + 2] > column2[column2_count]:
                if column2[column2_count + 2] + column2[column2_count] > column2[column2_count + 1]:
                    count += 1

        column2_count += 3

    while column3_count + 2 < column3.__len__():
        if column3[column3_count] + column3[column3_count + 1] > column3[column3_count + 2]:
            if column3[column3_count + 1] + column3[column3_count + 2] > column3[column3_count]:
                if column3[column3_count + 2] + column3[column3_count] > column3[column3_count + 1]:
                    count += 1

        column3_count += 3

    print(count)
