def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    for number in xrange(25):
        sum_of_last_3_elements = 0
        for number in lst[-3:]:
            sum_of_last_3_elements += number
        lst.append(sum_of_last_3_elements)

sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]