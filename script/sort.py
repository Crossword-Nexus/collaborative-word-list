#!/usr/bin/python3

import csv

FILENAME = 'xwordlist.dict'

def read():
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f, fieldnames=['word', 'score'], delimiter=";")
        parsed = []
        has_error = False
        word_to_line = {}
        for index, row in enumerate([r for r in reader]):
            word, score = row['word'], row['score']
            if word is None:  # Ignore blank lines
                continue
            if score is None:
                print(f"has_error -- Missing score for {word} on line {index + 1}")
                has_error = True
                continue
            score = int(score.strip())
            word = word.upper().strip()
            if word in word_to_line:
                print(f"has_error -- Word {word} on lines ({word_to_line[word]}, {index + 1})" \
                       + " is in dictionary more than once")
                has_error = True
                continue

            parsed.append({"word": word, "score": score})
            word_to_line[word] = index + 1
        if has_error:
            print("\n")
            raise Exception("See above errors")
        return parsed

def sort(words):
    return sorted(words, key=lambda x: (-x['score'], x['word']))

def write(sorted_words):
    with open(FILENAME, 'w') as f:
        # Sort by score desc first, then alphabetically
        writer = csv.DictWriter(f, fieldnames=['word', 'score'], delimiter=";")
        for w in sorted_words:
            writer.writerow(w)
        print(f"Successfully sorted dictionary with {len(words)} words!")


if __name__ == '__main__':
    words = sort(read())

    # Double-check the list is roughly as long as expected
    assert len(words) > 425000, f"Word list is too short ({len(words)} words), cancelling"

    write(words)


