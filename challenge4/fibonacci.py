
def int_to_english(num):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}
    k = 1000
    mill = k * 1000
    bill = mill * 1000
    trill = bill * 1000

    assert (0 <= num)

    if num < 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + ' ' + d[num % 10]

    if num < k:
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred and ' + int_to_english(num % 100)

    if num < mill:
        if num % k == 0:
            return int_to_english(num // k) + ' thousand'
        else:
            return int_to_english(num // k) + ' thousand, ' + int_to_english(num % k)

    if num < bill:
        if (num % mill) == 0:
            return int_to_english(num // mill) + ' million'
        else:
            return int_to_english(num // mill) + ' million, ' + int_to_english(num % mill)

    if num < trill:
        if (num % bill) == 0:
            return int_to_english(num // bill) + ' billion'
        else:
            return int_to_english(num // bill) + ' billion, ' + int_to_english(num % bill)

    if num % trill == 0:
        return int_to_english(num // trill) + ' trillion'
    else:
        return int_to_english(num // trill) + ' trillion, ' + int_to_english(num % trill)

    raise AssertionError('num is too large: %s' % str(num))


def fibonacci3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


number = 0
sequence = 12
# select sequence value above
for i in fibonacci3():
    if number >= sequence or sequence >= 1000:
        break
    if number <= sequence:
        text = int_to_english(i)
        print('Sequence of:', number + 1, ' Value:', i, '- ' + text)
    else:
        break
    number += 1



