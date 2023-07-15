# LC 1732
# Find the highest altitude a biker reaches along his path, where they start at 0 altitude
# and gain[i] = altitude change from point i to i+1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest = -10000
        current_altitude = 0

        for item in gain:
            current_altitude += item
            # Can use max() but this saves on function call overhead
            if current_altitude > highest:
                highest = current_altitude

        return max(highest, 0)
