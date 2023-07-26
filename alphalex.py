'''
Longest word finder for bookworm adventures deluxe.
'''

import argparse


def get_playable_words(words, letters):
    ''' Find the subset of words in `words` that can be made of `letters`,
    playable in bookworm adventures '''
    valid_words = []

    for word in words:
        temp_word = word.lower()
        # Erase each letter once and then see if we have an empty string
        for letter in letters:
            temp_word = temp_word.replace(letter, '', 1)
        if temp_word == '':
            valid_words.append(word)
    return valid_words


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

    # Get and print letters
    playable_words = get_playable_words(words, letters)
    for word in sorted(playable_words, key=lambda x: len(x)):
        print(word)


if __name__ == '__main__':
    main()
