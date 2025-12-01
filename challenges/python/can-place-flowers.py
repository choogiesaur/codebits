# works but clean this tf up
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
        elif len(flowerbed) == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n -= 1
        else:
            # mark first one or dont
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            for i in range(1, len(flowerbed)-2):
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                n -= 1
        print(n)
        if n <= 0:
            return True
        else:
            return False

                
