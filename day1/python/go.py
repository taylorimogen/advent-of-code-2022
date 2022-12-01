# Each elf is carrying a certain number of calories
# Data set: one item per line gives a number which represents number of calories
# Each Elf separates their own inventory from the previous elf's inventory with a blank line
# The elves would like to know how many calories are being carried by the elf with the most calories

class MostCalorificElf:
    def __init__(self, file):
        self.file = file

    def return_most_calorific_elf(self):
        with open(self.file, mode='r') as file:
            all_elf_calories = file.read().splitlines()
            all_elf_calories_sum = []
            single_elf_calories = []
            for item in all_elf_calories:
                if item:
                    single_elf_calories.append(int(item))
                else:
                    all_elf_calories_sum.append(sum(single_elf_calories))
                    single_elf_calories = []
                    continue

            print(max(all_elf_calories_sum))



if __name__ == '__main__':
    MostCalorificElf("../input.txt").return_most_calorific_elf()