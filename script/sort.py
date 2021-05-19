#!/usr/bin/python3

import csv

FILENAME = 'xwordlist.dict'

def read():
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f, fieldnames=['word', 'score'], delimiter=";")
        d = []
        error = False
        word_to_line = {}
        for index, row in enumerate([r for r in reader]):
            # Ignore blank lines
            if row['word'] is None:
                continue
            if row['score'] is None:
                print(f"ERROR -- Missing score for {row['word']} on line {index + 1}")
                error = True
                continue
            row['score'] = int(row['score'].strip())
            row['word'] = row['word'].upper().strip()
            if row['word'] in word_to_line:
                print(f"ERROR -- Word {row['word']} on lines ({word_to_line[row['word']]}, {index + 1})" \
                       + " is in dictionary more than once")
                error = True
                continue

            d.append(row)
            word_to_line[row['word']] = index + 1
        if error:
            print("\n")
            raise Exception("See above errors")
        return d

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
    words = read()
    words = sort(words)

    # Double-check the list is roughly as long as expected
    assert len(words) > 425000, f"Word list is too short ({len(words)} words), cancelling"

    write(words)


