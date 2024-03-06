import csv
with open("/usr/share/dict/words") as f:
    words = f.read().splitlines()

first_bad = list("bcdfghjklmnpqrstvwxyz")
second_bad = list("dhjklmnqruvwxyz")
third_bad = second_bad
fourth_bad = list("acfgjkquvwxyz")

four_letters = [word for word in words if len(word) == 4]
cleaned = [word for word in four_letters if
           word[0] not in first_bad and
           word[0].lower() == word[0] and
           word[1] not in second_bad and
           word[2] not in third_bad and
           word[3] not in fourth_bad]


def generate_possibilities(word_list: list):
    new_grid = [[first_word, "blue", third_word] for first_word in word_list for third_word in word_list]
    reshaped_grid = list(map(list, zip(*new_grid)))
    unique_combos = []
    for col_idx in range(len(reshaped_grid[0])):  # Iterate over the number of columns
        column = [row[col_idx] for row in reshaped_grid]  # Extract the column
        building_string = ''
        for word in column:
            building_string = building_string + (word[0])
        unique_combos.append(building_string)
    unique_combos = set(unique_combos)
    return sorted(list(unique_combos))


def make_csv(word_grid: list):
    file = "possible_words" + ".csv"
    with open(file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in word_grid:
            writer.writerow(row)


four_letter_combos = generate_possibilities(cleaned)
make_csv(four_letter_combos)
