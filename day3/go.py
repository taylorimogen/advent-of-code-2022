# two compartments per elf rucksack
# Each item must go in one of two compartments depending on what it is. These have been muddled, one item exactly is repeated over both items
# input: items in each rucksack - characters per line represent each one
# given rucksack: same no. of items in each compartment - first half of characters is what's in the first compartment
# priority rating: a-z have priority 1-26, A-Z have priority 27-52
# Find the item that appears in both compartments, and sum the priorities

FILENAME = 'input.txt'

class Priorities:
    """
    Dictionary for priority ratings for each item
    """
    priority_dict = {}

    def create_priority_dict(self):
        # use ord and chr to iterate over letters of the alphabet
        priority = 1
        for i in range(ord('a'), ord('z') + 1):
            self.priority_dict[chr(i)] = priority
            self.priority_dict[chr(i).upper()] = priority + 26
            priority += 1

class SumItemPriorities:
    """
    Methods for calculating the sum of the priority ratings of duplicated items across both compartments
    """
    rucksacks = []

    def __init__(self, rucksacks):
        self.rucksacks = rucksacks

    def sum_duplicated_item_priorities(self):
        priorities = []
        for rucksack in self.rucksacks:
            [first, second] = self.split_into_compartments(rucksack)
            duplicate = self.get_intersection(first, second)
            priorities.append(Priorities().priority_dict.get(duplicate))
        return sum(priorities)

    def split_into_compartments(self, rucksack_items):
        half = int(len(rucksack_items)/2)
        return [rucksack_items[:half], rucksack_items[half:]]

    def get_intersection(self, first, second):
        intersection = set(first).intersection(second)
        return ''.join(intersection)

def list_items_rucksacks():
    """
    Read in rucksack items for each elf
    """
    with open(FILENAME, mode='r') as file:
        rucksacks = file.read().splitlines()
    return rucksacks

if __name__ == '__main__':
    Priorities().create_priority_dict()
    rucksacks = list_items_rucksacks()
    print(SumItemPriorities(rucksacks).sum_duplicated_item_priorities())
