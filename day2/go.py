

class RockPaperScissors:
    # total score = sum of scores for each round
    # score is 1 for rock, 2 for paper, 3 for scissors
    # you get 0 if you lose, 3 if it was a draw and 6 if you won
    # A,X = rock ; B,Y = paper ; C,Z = scissors
    # example game: ABC, YXZ - three rounds
    # round 1: opponent chooses rock, and you should choose paper (score: 2 + 6)
    # round 2: opponent chooses paper, and you should choose rock (score: 1 + 0)
    # round 3: opponent chooses scissors, and you choose scissors, (score: 3 + 3)
    # Total score = 15


    def read_in_strategy(self, file):
        with open(file, mode='r') as strategy:
            pass
            # read in as a list, dict?
            all_lines = strategy.read()
            # replace opponent's letters with same as for me
            new_lines = all_lines.replace('A', 'X')
            new_lines = new_lines.replace('B', 'Y')
            new_lines = new_lines.replace('C', 'Z')

            total_score = 0
            for line in new_lines.splitlines():
                # draw
                if line[0] == line[2]:
                    total_score += 3

                if line[2] == 'X':
                    total_score += 1
                    # if I play rock and they play scissors
                    if line[0] == 'Z':
                        total_score += 6

                elif line[2] == 'Y':
                    total_score += 2
                    # if I play paper and they play rock
                    if line[0] == 'X':
                        total_score += 6
                else:
                    total_score += 3
                    # if I play scissors and they play paper
                    if line[0] == 'Y':
                        total_score +=6

        return total_score



if __name__ == '__main__':
    total_score = RockPaperScissors().read_in_strategy("input.txt")
    print(total_score)