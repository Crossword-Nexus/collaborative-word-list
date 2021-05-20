#!/usr/bin/python3

import unicodedata

FILENAME = 'xwordlist.dict'

def strip_accents(s):
    """String accents from a string"""
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def read():
    parsed = []
    used_words = set()
    with open(FILENAME, 'r') as f:
        for line in f:
            # Remove leading and trailing whitespace
            line = line.strip()
            # Split out the word and score
            try:
                word, score = line.split(';')
            except:
                continue
            # Don't bother if we don't have a word
            if not word:
                continue
                
            ## Normalize the word ##
            # Strip extraneous whitespace
            word = word.strip()
            # Strip accents
            word = strip_accents(word)
            # Make uppercase
            word = word.upper()
            # Remove any non-alphanumeric characters
            word = ''.join(c for c in word if c.isalnum())
            
            # Don't bother if we don't have a score
            if score is None:
                continue
            # Cast score as an int
            score = int(score.strip())
            
            # Don't use words more than once
            if word in used_words:
                continue
            else:
                used_words.add(word)
            
            # Add this word to our collection 
            parsed.append({"word": word, "score": score})
    return parsed

def sort(words):
    return sorted(words, key=lambda x: x['word'])

def write(sorted_words):
    with open(FILENAME, 'w') as f:
        for w in sorted_words:
            word, score = w['word'] ,w['score']
            f.write(f'{word};{score}\n')
        print(f"Successfully sorted dictionary with {len(words)} words!")


if __name__ == '__main__':
    words = sort(read())

    # Double-check the list is roughly as long as expected
    assert len(words) > 425000, f"Word list is too short ({len(words)} words), cancelling"

    write(words)


