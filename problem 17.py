
#
one2hundred_dict = {0: ('', 'Ten'),
                    1: ('One', 'Eleven'),
                    2: ('Two', 'Twelve', 'Twenty'),
                    3: ('Three', 'thirteen', 'Thirty'),
                    4: ('Four', 'Fourteen', 'Forty'),
                    5: ('Five', 'Fifteen', 'Fifty'),
                    6: ('Six', 'Sixteen', 'Sixty'),
                    7: ('Seven', 'Seventeen', 'Seventy'),
                    8: ('Eight', 'Eighteen', 'Eighty'),
                    9: ('Nine', 'Nineteen', 'Ninety')
                    }

def two_digits(str_num):
    if len(str_num) == 1:
        ones = int(str_num[0])    # ones = rows
        tens = 0                  # tens = columns
    else:
        tens = int(str_num[0])
        ones = int(str_num[1])
    if tens == 0 or tens == 1:
        return one2hundred_dict[ones][tens]
    else:
        word = one2hundred_dict[tens][2]
        word += ' ' + one2hundred_dict[ones][0]
        return word

def three_digits(str_num):
    hundreds = int(str_num[0])
    if hundreds == 0:
        return two_digits((str_num)[-2:])
    tens_ones = str_num[1:]
    word = one2hundred_dict[hundreds][0] + ' ' + 'Hundred'
    if tens_ones != '00':
        word += ' and ' + two_digits(tens_ones)
    return word


def wordToNum(num):
    word_list = ['','Thousand','Million','Billion']

    Words = ''
    if num == '0':
        Words = one2hundred_dict[0][0]
    else:
        while len(num) > 0:
            while num[0] == '0':
                num = num[1:]
            indx = int((len(num) -1) / 3 )
            pos = len(num) % 3
            if pos == 0:
                pos = 3
                word = three_digits(num[:pos]) + ' ' + word_list[indx]
            else:
                word = two_digits(num[:pos]) + ' ' + word_list[indx]
            if Words:
                Words += ' ' + word
            else:
                Words = word
            num = num[pos:]
    return Words



listOfWords = []
for x in range(0,1000):
    num = str(x)
    word = (wordToNum(num))
    listOfWords.append(len(word) - word.count(' '))

print(sum(listOfWords))

one Thousand