class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0) return 0;
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        int count = 0;
        int temp = 0;
        for(int i = 0; i<nums.length-1; i++){
            if(nums[i]==nums[i+1]) continue;
            if(nums[i]==nums[i+1]-1 ){
                count++;
                if(count>temp){
                temp=count;
            }
            }else{
                count = 0;
            }
            
        }
        return temp+1;
    }
}