# Each elf is carrying a certain number of calories
# Data set: one item per line gives a number which represents number of calories
# Each Elf separates their own inventory from the previous elf's inventory with a blank line
# The elves would like to know how many calories are being carried by the elf with the most calories


def read_in_file(file):
    with open(file, mode='r') as input:
        input.read().splitlines()
    return input

def return_most_calorific_elf(input):
    current_elf_calories = 0
    all_elf_calories = []
    for item in input:
        if item:
            current_elf_calories += int(item)
        else:
            all_elf_calories.append(current_elf_calories)
            current_elf_calories = 0

    return max(all_elf_calories)


import sys
if __name__ == '__main__':
    if sys.argv[1]:
        input = read_in_file(sys.argv[1])
        print(return_most_calorific_elf(input))
