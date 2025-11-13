# lc 443
# string comp
# "aabbccccd" ->
# "a2b2c4d"
class Solution:
    def compress(self, chars: List[str]) -> int:
        write_ptr = 0
        read_ptr = 0
        while read_ptr < len(chars):
            curr = chars[read_ptr]

            # Determine length of group
            count = 0
            while read_ptr < len(chars) and chars[read_ptr] == curr:
                count += 1
                read_ptr += 1

            # write group label first
            chars[write_ptr] = curr
            write_ptr += 1

            if count > 1:
                for char in str(count):
                    chars[write_ptr] = char
                    write_ptr += 1
        
        return write_ptr
