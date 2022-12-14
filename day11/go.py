# each monkey has attributes:
# worry level for each item the monkey is holding in the order they're inspected
# operation shows how your worry changes from before inspection to after
# test shows how the monkey will use your worry level

# order: gauge worry level, inspect item, test worry level
# after inspecting item, divide by three and round to nearest int
# each monkey takes turns inspecting and throwing items.
# monkey 0 goes first, inspects and throws item 1, inspects and throws item 2...
# monkey 0 can throw item 5 to monkey 3, then that does on the end of monkey 5's list
# keep track of number of times a monkey has inspected an item
# after 20 rounds, who are the two most active monkeys? Times this together

class Monkeys:
    # keys: monkey ids, values: Monkey class
    dict = {}

class Monkey:

    def __init__(self):
        self.id = 0
        self.item_worry = []
        self.operation = ''
        self.test_number = 0
        self.throw_to_true = -1
        self.throw_to_false = -1
        self.inspections = 0
        self.activity = 0

    def reduce_worry(self, worry):
        # use double slash for floor division
        return worry // 3

    def perform_operation(self, worry):
        num1 = int(self.operation[0]) if self.operation[0] != 'old' else worry
        num2 = int(self.operation[2]) if self.operation[2] != 'old' else worry
        if self.operation[1] == '*':
            return num1 * num2
        elif self.operation[1] == '+':
            return num1 + num2

    def test_worry_level(self, worry, index):
        # throw the item from this monkey
        self.item_worry[index] = '_'
        # decide which monkey to throw it to
        if worry % self.test_number == 0:
            return self.throw_to_true
        else:
            return self.throw_to_false


    def take_turn(self):
        for i in range(len(self.item_worry)):
            worry = self.perform_operation(self.item_worry[i])
            worry = self.reduce_worry(worry)
            throw_to_monkey = self.test_worry_level(worry, i)
            self.activity +=1
            update_monkey_items(throw_to_monkey, worry)
        self.item_worry = [x for x in self.item_worry if x != '_']



def capture_monkey_attributes(input):
    new_monkey = Monkey()
    for i in range(len(input)):
        line = input[i].strip(':').split()
        if 'Monkey' in line:
            new_monkey.id = int(line[1])
        elif 'Starting' in line:
            new_monkey.item_worry = list(map(lambda x: int(x.strip(',')), line[2:]))
        elif 'Operation:' in line:
            new_monkey.operation = line[3:]
        elif 'Test:' in line:
            new_monkey.test_number = int(line[-1])
        elif 'true:' in line:
            new_monkey.throw_to_true = int(line[5])
        elif 'false:' in line:
            new_monkey.throw_to_false = int(line[5])
            Monkeys.dict[int(new_monkey.id)] = new_monkey
            new_monkey = Monkey()

def update_monkey_items(throw_to_monkey, worry_val):
    """

    :param throw_to_monkey:
    :return:
    """
    print("Throwing to monkey number", throw_to_monkey)
    print("before throw:",Monkeys.dict.get(throw_to_monkey).item_worry)
    Monkeys.dict[throw_to_monkey].item_worry = Monkeys.dict.get(throw_to_monkey).item_worry + [worry_val]
    print("after throw",Monkeys.dict.get(throw_to_monkey).item_worry)
    # Monkeys.dict.get(throw_to_monkey).item_worry += [worry_val]

def complete_one_round():
    for key,value in Monkeys.dict.items():
        value.take_turn()

def complete_20_rounds():
    for i in range(20):
        complete_one_round()

def find_most_active_monkeys():
    inspections = {}
    for key,value in Monkeys.dict.items():
        inspections[value.activity] = key
    maxi = max(inspections.keys())
    inspections.pop(maxi)
    maxi_2 = max(inspections.keys())
    return maxi*maxi_2


def read_in_file(file):
    with open(file, mode='r') as input:
        input = input.read().splitlines()
    return input



import sys
if __name__ == '__main__':
    if sys.argv[1]:
        input = read_in_file(sys.argv[1])
        capture_monkey_attributes(input)
        complete_20_rounds()
        print(find_most_active_monkeys())

    else:
        print("Please pass in the puzzle input")