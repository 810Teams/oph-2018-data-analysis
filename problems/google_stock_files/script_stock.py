"""
    Google Stock Problem
    Score Calculation Script

    - Ranging from answer not more than 5 will get full score.
    - Ranging from answer more than 5 but less than 15 will get decreasing score.
"""

def main():
    """ Main function """
    corrects = [803.210022, 802.330017, 813.330017, 808.679993, 808.01001,
                809.099976, 815.719971, 813.369995, 809.280029, 818.309998]

    scores = [calculate(float(input()), i, 5, 10) for i in corrects]

    print('-- Result --')
    print(', '.join([str(round(i, 2)) for i in scores]))
    print('Total: {:.2f}'.format(sum(scores)))

def calculate(answer, correct, r_full, r_loss):
    """ Calculate score """
    if correct - r_full <= answer <= correct + r_full:
        return 1.5
    elif answer < correct - r_full:
        return max((r_loss - abs(correct - r_full - answer))/r_loss, 0) * 1.5
    elif answer > correct + r_full:
        return max((r_loss - abs(correct + r_full - answer))/r_loss, 0) * 1.5

main()
