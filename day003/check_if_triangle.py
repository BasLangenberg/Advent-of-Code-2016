if __name__ == '__main__':
    count = 0
    with open('input_day3.txt','r') as file:
        for line in file:
            collection = line.rstrip('\n').split(',')
            num1, num2, num3 = int(collection[0]), int(collection[1]), int(collection[2])

            if num1 + num2 > num3:
                if num2 + num3 > num1:
                    if num3 + num1 > num2:
                        count += 1

    print(count)