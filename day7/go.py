# no space left on device
# all directories under root directory '/'
# the input represents commands in the terminal
# disk is full, so you want to find directories you can delete
# total size of each directory = sum(sizes of its files)
# find all the directories with a total size of at most 100000, and sum those - what is the total size?
import sys


class FindSumDirectorySizes:

    def __init__(self, file):
        self.file = file
        self.input = self.read_in_file()
        self.directory_sizes = {}

    def read_in_file(self):
        """ Read in text file and split into list of bash commands"""
        with open(self.file, mode="r") as file:
            input = file.read().split('$')
        return input


    def find_directory_sizes(self):
        """ Add sizes of each directory to dictionary """
        current_dir = []
        # for each ls command, capture the current directory and running total
        # and for each subdirectory, add the running total to parent directories as well
        for item in self.input:
            item = item.strip().split()
            if not item:
                continue
            if item[0] == 'cd':
                if item[1] == '..':
                    current_dir.pop()
                else:
                    current_dir.append(item[1])
            # sum the size of the files in the current directory
            if item[0] == 'ls':
                running_total = sum(int(x) for x in item[1::2] if x != 'dir')
            # update the size of the current directory and parent directories
                # for each path, add to dictionary and update parents. e.g. for /a/b, update /, /a, /a/b
                for i in range(0,len(current_dir)):
                    if i == 0:
                        path = '/'
                    else:
                        path = '/'.join(current_dir[:i+1])[1:]
                    print("current path:", current_dir[:i+1])
                    print("path:",path)
                    self.directory_sizes[path] = self.directory_sizes.get(path, 0) + running_total


    def sum_directory_sizes(self):
        """ Sum the directories of size smaller than 100000"""
        return sum(x for x in self.directory_sizes.values() if x <= 100000)


if __name__ == '__main__':
    if sys.argv[1]:
        find_sum = FindSumDirectorySizes(sys.argv[1])
        find_sum.find_directory_sizes()
        print(find_sum.directory_sizes)
        print("The sum of the directories of size under 100,000 is: ",find_sum.sum_directory_sizes())

    else:
        print("Please pass in the input file")
