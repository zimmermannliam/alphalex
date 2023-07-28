'''
Longest word finder for bookworm adventures deluxe.
'''

import argparse


def get_playable_words(words, letters):
    ''' Find the subset of words in `words` that can be made of `letters`,
    playable in bookworm adventures '''
    valid_words = []

    for word in words:
        temp_word = word
        # Erase each letter once and then see if we have an empty string
        for letter in letters:
            temp_word = temp_word.replace(letter, '', 1)
        if temp_word == '':
            valid_words.append(word)
    return valid_words


def bookworm_evaluate_letter(letter: str) -> float:
    ''' from https://bookwormadvs.fandom.com/wiki/Tile '''
    match letter:
        case 'a' | 'd' | 'e' | 'g' | 'i' | 'l' | 'n' | 'o' | 'r' | 's' | 't' | 'u':
            return 1
        case 'b' | 'c' | 'f' | 'h' | 'm' | 'p':
            return 1.25
        case 'v' | 'w' | 'y':
            return 1.5
        case 'j' | 'k' | 'q':
            return 1.75
        case 'x' | 'z':
            return 2
        case _:
            return 0

        

def bookworm_evaluate_word(word: str) -> int:
    ''' Sum of bookworm_evaluate_letter '''
    s = 0
    for letter in word:
        s += bookworm_evaluate_letter(letter)
    return s
        

def main():
    ''' Main functionality '''

    # Parse letters from arguments
    parser = argparse.ArgumentParser(
        prog='Lex',
        description='Beats bookworm adventures for you',
        epilog='Cheater!')
    parser.add_argument('letters',
                        help='Letters with spaces between them, e.x. g t w u i ...',
                        nargs='*')
    args = parser.parse_args()
    letters = args.letters

    # Get words from user dictionary
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().split('\n')

    # Get and print playable words in sorted order
    playable_words = get_playable_words(words, letters)
    for word in sorted(playable_words, key=bookworm_evaluate_word):
        print(f"{word}\t{bookworm_evaluate_word(word)}")


if __name__ == '__main__':
    main()
