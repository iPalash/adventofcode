word_2_dig = {"one":1, "two":2, "three":3, "four": 4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }


def detect_first_digit(word):
    i=0
    while i<len(word):
        if 48<=ord(word[i])<=57:
            return word[i]
        if word[i:i+3] in word_2_dig:
            return str(word_2_dig[word[i:i+3]])
        if word[i:i+4] in word_2_dig:
            return str(word_2_dig[word[i:i+4]])
        if word[i:i+5] in word_2_dig:
            return str(word_2_dig[word[i:i+5]])
        i+=1
    return ''

def detect_last_digit(word):
    i=len(word)-1
    while i>=0:
        if 48<=ord(word[i])<=57:
            return word[i]
        if word[i:i+3] in word_2_dig:
            return str(word_2_dig[word[i:i+3]])
        if word[i:i+4] in word_2_dig:
            return str(word_2_dig[word[i:i+4]])
        if word[i:i+5] in word_2_dig:
            return str(word_2_dig[word[i:i+5]])
        i-=1
    return ''


def extract_calibration_value(word):
    return int(detect_first_digit(word)+detect_last_digit(word))


import sys
filename = sys.argv[1]

with open(filename,'r') as f:
    data = f.read().split("\n")
    sm = 0
    for line in data:
        sm += extract_calibration_value(line)
    print(sm)