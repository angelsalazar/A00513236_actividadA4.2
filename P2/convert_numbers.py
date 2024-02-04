""" Converter """

import sys
import time

start_time = time.time()

if __name__ == '__main__':
    [_, * file_names] = sys.argv
    NUMBER_BITS = 16
    HEX_CHARS = '0123456789ABCDEF'
    FALLBACK_VALUE = '#VALUE!'
    summaries = []

    for file_name in file_names:
        with open(file_name, 'r', encoding='UTF-8') as file:
            raw_data = file.readlines()
            INDEX = 1
            summary = [
                ' '.join([
                    file_name.replace('.txt', ''),
                    'NUMBER',
                    'BIN',
                    'HEX'
                ])
            ]
            for entry in raw_data:
                entry = entry.strip()
                PARSED_ENTRY = None

                try:
                    PARSED_ENTRY = float(entry)
                except ValueError:
                    print(f'Invalid number {entry}')
                    PARSED_ENTRY = FALLBACK_VALUE
                # skip to next iteration if entry could not be parsed
                if PARSED_ENTRY == FALLBACK_VALUE:
                    summary.append(' '.join([str(INDEX), entry, PARSED_ENTRY, PARSED_ENTRY]))
                    INDEX += 1
                    continue
                # skip to next iteration if entry is 0
                if PARSED_ENTRY == 0:
                    summary.append(' '.join([str(INDEX), entry, '0', '0']))
                    INDEX += 1
                    continue
                BINARY = ''
                HEXADECIMAL = ''
                parsed_entry_bin = PARSED_ENTRY
                parsed_entry_hex = PARSED_ENTRY
                IS_NEGATIVE = False

                if PARSED_ENTRY < 0:
                    IS_NEGATIVE = True
                    parsed_entry_bin = abs(PARSED_ENTRY)

                # convert decimal to BINARY
                while parsed_entry_bin > 0:
                    BINARY = str(int(parsed_entry_bin % 2)) + BINARY
                    parsed_entry_bin = parsed_entry_bin // 2
                if IS_NEGATIVE:
                    BINARY = ''.join('1' if bit == '0' else '0' for bit in BINARY)
                    RESULT = ''
                    BIN1 = BINARY
                    BIN2 = '1'
                    CARRY = 0
                    i = len(BINARY) - 1
                    j = 0
                    while i >= 0 or j >= 0 or CARRY:
                        if i >= 0:
                            CARRY += int(BIN1[i])
                            i -= 1
                        if j >= 0:
                            CARRY += int(BIN2[j])
                            j -= 1
                        RESULT = str(CARRY % 2) + RESULT
                        CARRY //= 2
                    BINARY = RESULT
                    BINARY = ('1' * (10 - len(BINARY))) + BINARY
                # convert decimal to HEXADECIMAL
                MAX_VALUE = 2 ** NUMBER_BITS - 1
                RESULT = parsed_entry_hex % (MAX_VALUE + 1)
                while RESULT > 0:
                    rest = RESULT % 16
                    HEXADECIMAL = HEX_CHARS[int(rest)] + HEXADECIMAL
                    RESULT = RESULT // 16
                if IS_NEGATIVE:
                    HEXADECIMAL = ('F' * (10 - len(HEXADECIMAL))) + HEXADECIMAL
                summary.append(' '.join([str(INDEX), entry, BINARY, HEXADECIMAL]))
                INDEX += 1
            summaries.append('\n'.join(summary))
        summaries.append('execution time: ' + str(time.time() - start_time) + 's')
        SERIALIZED_SUMMARY = '\n\n'.join(summaries)
        print(SERIALIZED_SUMMARY)
        with open('WordCountResults.txt', 'w', encoding='UTF-8') as file:
            file.write(SERIALIZED_SUMMARY)
