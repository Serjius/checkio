import re


VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
NUMBERS = '1234567890'


def checkio(text):
    stipe_count = 0
    r = re.compile(r'[\s{}]+'.format(re.escape('.,')))
    for i in r.split(text.upper()):
        if len(i) <= 1 or i[0] in NUMBERS:
            continue
        is_vowels = i[0] in VOWELS
        is_stripe = True
        for j in range(1, len(i)):
            if (i[j] in VOWELS and is_vowels) or (i[j] in CONSONANTS and not is_vowels) or (i[j] in NUMBERS):
                is_stripe = False
                break
            else:
                is_vowels = i[j] in VOWELS
        if is_stripe:
            stipe_count += 1
    return(stipe_count)

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio("1st 2a ab3er root rate") == 1
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("1 2 3 12 13") == 0
