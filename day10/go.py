# replace the video system on listening device
# clock circuit ticks at a constant rate, each tick is a cycle
# figure out signal sent by CPU
# CPU has a register: X, starts with value: 1
# instructions: addx V - takes two cycles to complete, after this, X register is increased by value V
# noop takes one cycle to complete
# input the instructions to tell the CPU what to do
# e.g.
# noop; addx 3; addx -5
# During the first cycle, X is 1, after the first cycle, noop instruction finishes executiion
# At the second cycle, addx 3 begins, so during the third cycle, X goes from 1 to 4
# takes two cycles to complete, so is complete during third cycle, then addx -5 starts, so once we reach the fifth cycle
# V becomes -1
# Multiply the register by the cycle number to get the signal strength, get the sum of the signal strengths


def read_in_file(file):
    """
    Read in puzzle input
    :return:
    """
    with open(file, mode='r') as input:
        input = input.readlines()
    return input

def find_signal_strength(input):
    cycle_num = register_val = 1
    signal_strengths = []
    instruction_complete = False
    i = 0
    while(i < len(input)):
        # don't move on to the next command for two cycles if adding to the register value
        if 'addx' in input[i]:
            if instruction_complete:
                register_val += int(input[i].split()[1])
                i += 1
                instruction_complete = False
            else:
                instruction_complete = True
        # move on to the next command in the next cycle
        else:
            i += 1

        # increment cycle number each time go into while loop
        cycle_num += 1

        # capture signal strengths at required cycle points
        if cycle_num in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle_num*register_val)

    return sum(signal_strengths)



import sys

if __name__ == '__main__':
    if sys.argv[1]:
        input = read_in_file(sys.argv[1])
        print(find_signal_strength(input))
    else:
        print("Please enter the input for this problem")