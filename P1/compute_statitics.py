""" Compute Statitics """

import sys
import time

start_time = time.time()

if __name__ == '__main__':
    # reading arguments
    [_, * file_names] = sys.argv
    statitics_by_file_name = {}
    summaries = []
    for file_name in file_names:
        numbers = []
        TOTAL_NUMBERS = 0
        statitics = {}
        with open(file_name, 'r', encoding='UTF-8') as file:
            raw_data = file.readlines()
            TOTAL_NUMBERS = len(raw_data)
            for entry in raw_data:
                try:
                    numbers.append(float(entry))
                except ValueError:
                    print(f'Invalid number {entry}')
                # original_raw_entry = RAW_ENTRY
                # # parses the given raw_entry text by removing any char
                # # that is not a digit, plus sign, minus sign, and period
                # number_matched = re.search(r'[-+]?\d*\.?\d+', RAW_ENTRY)

                # # if raw_entry got parsed, then retrieve the matching group
                # # else default raw_entry to 0
                # if number_matched:
                #     RAW_ENTRY = number_matched.group()
                # else:
                #     RAW_ENTRY = 0

                # try:
                #     numbers.append(float(RAW_ENTRY))
                # except TypeError:
                #     print(f'Invalid number provided {original_raw_entry}')
        # saves file name
        statitics['TC'] = file_name.replace('.txt', '')

        # computes the count
        NUMBERS_SIZE = len(numbers)
        statitics['COUNT'] = TOTAL_NUMBERS

        # computes the mean
        statitics['MEAN'] = sum(numbers) / NUMBERS_SIZE

        # computes the median
        MID = NUMBERS_SIZE // 2
        sorted_numbers = sorted(numbers)
        if NUMBERS_SIZE % 2 == 0:
            mid_average = sorted_numbers[MID - 1] + sorted_numbers[MID]
            statitics['MEDIAN'] = mid_average / 2
        else:
            statitics['MEDIAN'] = sorted_numbers[MID]

        # computes the mode
        occurrences_by_number = {}
        MAX_OCCURRENCES = 1
        statitics['MODE'] = None
        for number in numbers:
            occurrences = occurrences_by_number.get(number, 0) + 1
            occurrences_by_number[number] = occurrences
            if occurrences_by_number[number] > MAX_OCCURRENCES and number != 0:
                MAX_OCCURRENCES = occurrences_by_number[number]
                statitics['MODE'] = number

        # computes the variance
        variance_number = []
        for number in numbers:
            variance_number.append((number - statitics['MEAN']) ** 2)
        statitics['VAR'] = sum(variance_number) / NUMBERS_SIZE

        # computes the standard deviation
        statitics['SD'] = statitics['VAR'] ** 0.5

        # save retrieved statitics
        summaries.append(statitics)
    # specifies how the summary data should be serialized
    keys = ['TC', 'COUNT', 'MEAN', 'MEDIAN', 'MODE', 'SD', 'VAR']

    rows = []
    for key in keys:
        cols = [key+'\t']
        for entry in summaries:
            if entry[key] is None:
                cols.append('N/A')
            else:
                cols.append(str(entry[key]))
        rows.append('\t'.join(cols))
    rows.append('execution time: ' + str(time.time() - start_time) + 's')
    SUMMARY = '\n'.join(rows)
    print(SUMMARY)
    with open('StatisticsResults.txt', 'w', encoding='UTF-8') as file:
        file.write(SUMMARY)
    