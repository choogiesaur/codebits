# For base 10 integer N, determine length of longest string of 0's in its binary representation
# Ex: 1041 -> 10000010001
# Longest string is 5 zeroes

def solution(N):
    # write your code in Python 3.6
    binary = "{0:b}".format(N)
    longest_gap_length = 0

    i = 0
    length = len(binary)

    while i < length:
        # Fast-forward past all 1's
        while i < length and binary[i] == '1':
            i += 1

        # Keep iterating, if 0 update current run length, if 1 break and reassess longest run
        current_gap_length = 0
        while i < length:
            if binary[i] == '0':
                current_gap_length += 1
            else:
                longest_gap_length = max(longest_gap_length, current_gap_length)
                break
            i += 1

    return longest_gap_length
