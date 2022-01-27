# A binary gap is a section of 0's surrounded by 1's in a number's binary representation
# EX: 
# 1001 -> Binary gap of length 2
# 10000101 -> Binary gap of length 4 and 1
# 1000 -> Technically not a binary gap
# Problem: Find the longest binary gap for input integer

# Not completely correct yet!
# Failed cases:
# trailing_zeroes
# n=6=110_2 and n=328=101001000_2
# simple3
# n=1162=10010001010_2 and n=5=101_2
# medium3
# n=66561=10000010000000001_2

def solution(N):
    # write your code in Python 3.6
    bin_rep = "{0:b}".format(N)
    # print(bin_rep)

    # Keep track of longest chain found
    longest = 0
    
    #Iterate characters in binary representation
    i = 0
    while i < len(bin_rep) - 1:

        # found 1 then 0; possible start of binary gap
        if bin_rep[i] == '1' and bin_rep[i+1] == '0':

            curr_chain_length = 0

            # increment to next char (wont go OoB)
            i += 1
                
            # continue iterating; for every zero encountered, increase curr chain length by 1
            while i < len(bin_rep):
                if bin_rep[i] == '0': 
                    curr_chain_length += 1
                    i += 1
                else:
                    # encountered a 1
                    if curr_chain_length > longest:
                        longest = curr_chain_length
                        i += 1
                    break
        i += 1
    return longest
