# LC 1071
# Logic of the loop:
# Want to assume strings are in order of length on each rep
# If not, order them correctly
# If strings are equal, return either as the GCD
# If longer starts with shorter, trim longer by one instance of shorter, then start loop again
# If at any point the longer str doesn't start with the shorter, there is no GCD
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str2) < len(str1):
            return self.gcdOfStrings(str2,str1)
        
        if str1 == str2:
            return str1

        if str2.startswith(str1):
            return self.gcdOfStrings(str1,str2[len(str1):])

        return ""
        
    def gcdOfStrings_iterative(self, str1: str, str2: str) -> str:
        while str1:
            if len(str2) < len(str1):
                str1, str2 = str2, str1  # Swap if str1 is longer
            
            if str1 == str2:
                return str1

            if str2.startswith(str1):
                str2 = str2[len(str1):]  # Remove the prefix from str2
            else:
                return ""

        return str2
