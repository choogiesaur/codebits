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
    
    public int sumArray(int arr[], int start, int num){
        int sum = 0;
        for (int i = start; i < num; i++){
            sum += arr[i];
        }
        return sum;
    }
}
