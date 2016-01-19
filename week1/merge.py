"""Module for 2048 game merge function"""


def merge(line):
    """Merges line (which is an array of 2 power n's) according to 2048 game rules
    :parameter line
    """

    result_of_multiply = [0] * (len(line))

    counter = 0
    for index in xrange(len(line)):
        if line[index] != 0:
            result_of_multiply[counter] = line[index]
            counter += 1

    for index in xrange(len(result_of_multiply) - 1):
        if result_of_multiply[index] == result_of_multiply[index + 1]:
            result_of_multiply[index] *= 2
            result_of_multiply[index + 1] = 0

    final_result = [0] * (len(line))

    counter = 0
    for index in xrange(len(line)):
        if result_of_multiply[index] != 0:
            final_result[counter] = result_of_multiply[index]
            counter += 1

    return final_result