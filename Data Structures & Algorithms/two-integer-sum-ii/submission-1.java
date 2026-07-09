class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int k = numbers.length-1;
        while(i<k){
            int sum = numbers[i]+numbers[k];
            if(sum>target){
                k--;
                continue;
            }
            if(sum<target){
                i++;
                continue;
            }
            if(sum==target){
                int[] arr = new int[2];
                arr[0]=i+1;
                arr[1]=k+1;
                return arr;
            }

        }
        return new int[2];
    }
}
