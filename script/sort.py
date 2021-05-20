#!/usr/bin/python3

FILENAME = 'xwordlist.dict'

def read():
    parsed = []
    used_words = set()
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip()
            try:
                word, score = line.split(';')
            except:
                continue
            if not word:
                continue
            word = word.upper()
            if score is None:
                continue
            score = int(score.strip())
            word = word.upper().strip()
            if word in used_words:
                continue
            else:
                used_words.add(word)
                
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


