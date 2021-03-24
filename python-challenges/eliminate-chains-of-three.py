# You have a string. Any consecutive chars of 3 or more, delete. AKA: Pop matches of three like candy crush.
# "AAAB" -> "B"
# "AAABBB" -> ""
# "AAZZZA" -> "" because deleting z's created chain of a's

s = "aaaabbbcccaaaaazxxxqqqcccaaad"
chars = [c for c in s]

i = 0
just_deleted = False
while i < len(chars) - 2:
    print(i, chars)
    while len(chars) >= 3 and chars[i] == chars[i+1] == chars[i+2]:
        print("Deleting three characters: ", chars[i:i+3])
        del chars[i+2]
        del chars[i+1]
        del chars[i]
        just_deleted = True
    # Deleting possibly created a new chain, so go back
    # to first window where that chain could have formed
    if just_deleted:
        i = max(0, i-2) # subtract 2 but dont go past 0
    else:
        i += 1
    just_deleted = False

print(chars)
