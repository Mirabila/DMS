import math

def solve(n: int, broken: int) -> int:
    if (isBrokenVersion(1) == True):
        return 1
    dict = {}
    max = n
    min = 1
    mid = math.ceil((max + min) / 2)
    while(True):

        if isBrokenVersion(mid) == False:
            dict.update({mid: False})
            min = mid
            mid = math.ceil((max + min) / 2)
            if(mid == min):
                mid += 1

        else :
            if (dict.get(mid - 1) == False and dict.get(mid) == True):
                return mid
            else:
                dict.update({mid:True})
                max = mid
                mid = math.ceil((max + min) / 2)
                if (mid == max):
                    mid -= 1
