import hashlib

def find_passwd(input):
    result = ''
    count = 0
    while result.__len__() < 8:
        pos = 0
        pick = True
        while pos < 5:
            if hashlib.md5((input + str(count)).encode('utf-8')).hexdigest()[pos] is not '0':
                pick = False
                break
            else:
                pos += 1

        if pick:
            result += hashlib.md5(str(input + str(count)).encode('utf-8')).hexdigest()[5]

        count += 1

    return result

if __name__ == '__main__':
    print(find_passwd('reyedfim'))

    # Wrong: 18f47a30
    # Now  :

def test_find_password():
    assert find_passwd('abc') == '18f47a30'