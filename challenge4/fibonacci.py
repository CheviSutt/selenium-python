# def fibonacci1(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# def fibonacci2(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return a

# for i in range(1, 27):
#     print(fibonacci2(i))


def int_to_english(num):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

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

    if num < m:
        if num % k == 0:
            return int_to_english(num // k) + ' thousand'
        else:
            return int_to_english(num // k) + ' thousand, ' + int_to_english(num % k)

    if num < b:
        if (num % m) == 0:
            return int_to_english(num // m) + ' million'
        else:
            return int_to_english(num // m) + ' million, ' + int_to_english(num % m)

    if num < t:
        if (num % b) == 0:
            return int_to_english(num // b) + ' billion'
        else:
            return int_to_english(num // b) + ' billion, ' + int_to_english(num % b)

    if num % t == 0:
        return int_to_english(num // t) + ' trillion'
    else:
        return int_to_english(num // t) + ' trillion, ' + int_to_english(num % t)

    raise AssertionError('num is too large: %s' % str(num))


def fibonacci3():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


number = 0
for i in fibonacci3():
    if number >= 50:
        break
    if number <= 40:
        text = int_to_english(i)
        print(i, '- ' + text)
    else:
        print(i, "- number is above the 50th fibonacci sequence!")
    number += 1
