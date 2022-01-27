# DOES NOT PASS ALL CASES YET
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        clean = s.replace("-","").upper()
        
        num_groups = len(clean) // k
        init_len   = len(clean) %  k
        print(num_groups, init_len)
        
        # init_len = 3
        if init_len != 0:
            i = init_len
            reformatted = clean[:init_len] + "-"
        else:
            i = 0
            reformatted = ""
        
        while i < num_groups:
            # print("Indices:", i*k, (i+1)*k)
            segment = clean[i*k:(i+1)*k]
            # print(segment)
            reformatted += segment + "-"
            i += 1
            
        return reformatted[:len(reformatted)-1]
