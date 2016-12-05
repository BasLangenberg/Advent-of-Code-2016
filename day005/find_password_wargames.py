import hashlib

# https://www.youtube.com/watch?v=NHWjlCaIrQo&t=25

def find_passwd(input):
    result = ['_','_','_','_','_','_','_','_']
    taken = []
    count = 0
    while result.__contains__('_'):
        pos = 0
        pick = True
        while pos < 5:
            if hashlib.md5((input + str(count)).encode('utf-8')).hexdigest()[pos] is not '0':
                pick = False
                break
            else:
                pos += 1

        if pick:
            try:
                if int(hashlib.md5(str(input + str(count)).encode('utf-8')).hexdigest()[5]) < 8 \
                        and int(hashlib.md5(str(input + str(count)).encode('utf-8')).hexdigest()[5]) not in taken:
                    result[int(hashlib.md5(str(input + str(count)).encode('utf-8')).hexdigest()[5])] = \
                        hashlib.md5(str(input + str(count)).encode('utf-8')).hexdigest()[6]
                    taken.append(int(hashlib.md5(str(input + str(count)).encode('utf-8')).hexdigest()[5]))
            except:
                pass

        count += 1

    return ''.join(result)

if __name__ == '__main__':
    print(find_passwd('reyedfim'))

def test_find_password():
    assert find_passwd('abc') == '05ace8e3'