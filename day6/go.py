# malfunctioning communication device
# need to detect start of packet marker, indicated by a sequence of four characters that are all different
# identify the first position where the four most recently received characters are all different
# report the number of chars from the start to the end of the four char packet markers
# e.g. mjqjpqmgbljs, the marker appears after seven characters have been received, so the answer is seven

FILE = "input.txt"

class FindDeviceMalfunction:

    def read_in_file(self):
        """
        Read in puzzle input
        :return:
        """
        with open(FILE, mode='r') as input:
            input = input.read()
        return input

    def detect_packet_marker(self, input):
        """
        Find the index of the character that marks the end of the packet marker
        :return:
        """
        # build sets of characters of length four, until the set is of length 4
        for i in range(4,len(input)):
            current_set = set(input[i-4:i])
            if len(current_set) == 4:
                return i



if __name__ == '__main__':
    find_device_malfunction = FindDeviceMalfunction()
    input = find_device_malfunction.read_in_file()
    print(find_device_malfunction.detect_packet_marker(input))