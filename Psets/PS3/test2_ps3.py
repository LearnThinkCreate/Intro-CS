import random
import math

VOWELS = 'aeiou'

num_vowel = int(math.ceil(4/3))
    
## Trying to solve the problem using recursion
def add_vowel(num_vowel):
    if num_vowel == 1:
        ## The first vowel should always be a wildcard
        wildcard = new_letter[0]
        hand[wildcard] = hand.get(wildcard , 0 ) + 1
    else:
        add_vowel(num_vowel - 1)
        ## After there is already a wildcard, then add random vowels
        vowel = random.choice(VOWELS)
        hand[vowel] = hand.get(vowel,0) +1
        
        print(hand)
        
hand = {}
new_letter = ["*"]

add_vowel(num_vowel)