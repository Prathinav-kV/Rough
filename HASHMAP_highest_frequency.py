class Solution:

    def __init__(self, L : list[int]):

        self.l = L

    def freq(self)->int:

        a = dict()
        final,largest = -1,-1

        for i in self.l:
            a[i] = a.get(i,0) + 1
            if largest < a[i]:
                final, largest = i , a[i]
        return final
    
def main():

    nums = [1, 2, 2, 3, 3, 3]
    a = Solution(nums)
    largest = a.freq()
    print("Highest frequency : "+str(largest))

if __name__=="__main__":
    main()



