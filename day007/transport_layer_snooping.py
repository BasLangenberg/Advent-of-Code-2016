import re

def supports_tls(input):
    hypernet = re.findall(r'\[(.*?)\]', input)
    abba = []
    for hyper in re.findall(r'\[(.*?)\]', input):
        input = input.replace('[' + hyper + ']', '')

    for hyper in hypernet:
        if not hyper.__len__() % 4:
            count = 0
            if str(hyper[count] + hyper[count + 1]) == str(hyper[count+3] + hyper[count+2]):
                return False

    return True

def test_transport_layer_snooping():
    assert supports_tls('abba[mnop]qrst[312]') == True
    assert supports_tls('abcd[bddb]xyyx') == False
    assert supports_tls('aaaa[qwer]tyui') == False
    assert supports_tls('ioxxoj[asdfgh]zxcvbn') == False