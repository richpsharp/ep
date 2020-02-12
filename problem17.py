"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?
"""

NUMBERS_TO_WORDS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def number_to_word(n):
    """Convert number to word."""
    word = ''
    if n == 100:
        return 'hundred'
    if n == 1000:
        return 'thousand'
    if n > 100:
        word += NUMBERS_TO_WORDS[int(str(n)[0])] + 'hundred'
        n = n % 100
        if n == 0:
            return word
    if n in NUMBERS_TO_WORDS:
        return word + NUMBERS_TO_WORDS[n]
    if n < 100:
        ten_value = (n // 10) * 10
        if ten_value in NUMBERS_TO_WORDS:
            word += NUMBERS_TO_WORDS[ten_value]
        n = n % 10
    if n > 0:
        word += NUMBERS_TO_WORDS[n]
    return word


if __name__ == '__main__':
    for i in range(1, 300):
        print(number_to_word(i))
