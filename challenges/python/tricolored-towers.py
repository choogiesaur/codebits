# My solution to the Codility Tricolored Towers problem of March 2022
# I got the Codility Golden Award for the Year of the Tiger Challenge for this :)
# See the credential, problem, and solution statistics here:
# https://app.codility.com/cert/view/certFDR9GD-ABJXGNZHKAFXSFJW/

from collections import defaultdict

# For given string and input indices, generate the string
# resulting from swapping those blocks
def generate_swap(str, index1, index2):
    arr = [str[0], str[1], str[2]]
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr[0] + arr[1] + arr[2]

def solution(T):
    # For each stack, generate possible block combinations 
    # and update hashtable with their counts
    counts = defaultdict(int)
    highest_occurrences = 0

    for stack in T:
        alt_stack1 = generate_swap(stack, 0, 1)
        alt_stack2 = generate_swap(stack, 1, 2)

        counts[stack] += 1
        if alt_stack1 != stack:
            counts[alt_stack1] += 1
        if alt_stack2 != stack:
            counts[alt_stack2] += 1

        highest_occurrences = max(highest_occurrences, counts[stack], counts[alt_stack1], counts[alt_stack2])

    return highest_occurrences
