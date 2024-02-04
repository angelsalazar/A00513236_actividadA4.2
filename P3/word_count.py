""" Converter """

import sys
import time

start_time = time.time()

if __name__ == '__main__':
    [_, * file_names] = sys.argv
    summaries = []

    for file_name in file_names:
        occurrences_by_word = {}
        with open(file_name, 'r', encoding='UTF-8') as file:
            words = file.readlines()
            for word in words:
                word = word.strip()
                occurrences_by_word[word] = occurrences_by_word.get(word, 0) + 1

            rows = ['Rows Labels\t\tCount of ' + file_name.replace('.txt', '')]
            for key_pair in occurrences_by_word.items():
                rows.append(key_pair[0] + '\t\t' + str(key_pair[1]))
            rows.append('Grand Totat\t\t' + str(len(words)))
            summaries.append('\n'.join(rows))
    summaries.append('execution time: ' + str(time.time() - start_time) + 's')
    SUMMARY = '\n\n'.join(summaries)
    print(SUMMARY)
    with open('WordCountResults.txt', 'w', encoding='UTF-8') as file:
        file.write(SUMMARY)
