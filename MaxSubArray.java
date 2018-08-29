// given integer array, recursively find contiguous subarray with max sum
// times out on leetcode, there is a faster way
class MaxSubArray {
    public int maxSubArray(int[] nums) {
        int pos = 0;
        int num = nums.length;
        
        if(num == 1){
            return nums[pos];
        }
        else if(num == 0){
            return 0;
        }else{
            int sum = sumArray(nums, pos, num);
            //System.out.println("Sum: " + sum);
            //System.out.println("pos: " + pos + " num: " + num);
            int numLess = Math.max(sum, maxSubArray(Arrays.copyOfRange(nums, pos, pos+num-1))); //recursive call with shorter subarray
            int posMore = Math.max(sum, maxSubArray(Arrays.copyOfRange(nums, pos+1, pos+num))); // recursive call with next starting pos
            return Math.max(numLess,posMore);
        }
    }
    //helper function for above
    public int sumArray(int arr[], int start, int num){
        int sum = 0;
        for (int i = start; i < num; i++){
            sum += arr[i];
        }
        return sum;
    }
    
    // EDIT: Much faster solution! Derived from Jon Bentley (Sep. 1984 Vol. 27 No. 9 Communications of the ACM P885)
    public int maxSubArray(int[] nums) {
        int maxCur = nums[0];
        int maxYet = nums[0];
        for(int i = 1; i < nums.length; i++){
            maxCur = Math.max(maxCur+nums[i], nums[i]);
            maxYet = Math.max(maxCur, maxYet);
        }
        return maxYet;
    }
}

// a solution where you iterate over the array, keeping track of:
// a max subarray ending at current position    (maxCurr)
// and a max subarray so far                    (maxYet)
// at each step, the maxCurr is calculated as Max(maxCurr + next element, next element itself)
// since either you can grow a contiguous array that is greater, or start a new array from next element
// and the maxYet is simply updated if the maxCurr becomes greater

// trace: [-2,1,-3,4,-1,2,1,-5,4],
/*
MEH = -2
MSF = -2

MEH = Max(-2+1,1) = 1
MSF = Max(-2, 1) = 1

MEH = Max(1-3,-3) = -2
MSF = Max(1, -2) = 1

MEH = Max(-2+4, 4) = 4
MSF = Max(1, 4) = 4

MEH = Max(4-1,-1) = 3 
MSF = Max(4, 3) = 4

MEH = Max(3+2,2) = 5
MSF = Max(4, 5) = 5

MEH = Max(5+1,1) = 6
MSF = Max(5,6) = 6

MEH = Max(6-5, -5) = 1
MSF = Max(6, 1) = 6

MEH = Max(1+4, 4) = 4
MSF = Max(6, 4) = 6
*/
