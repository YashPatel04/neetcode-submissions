class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prod = 1;
        HashMap <Integer, Integer> set = new HashMap<>();
        int[] out = new int[nums.length];
        int zero = -1;
        int index = 0;
        for(int i = 0; i<nums.length; i++){
            set.put(i, nums[i]);
            if(nums[i]==0) {
                zero++;
                index = i;
                continue;
            }
            prod *= nums[i];
        }
        System.out.println(zero);
        if(zero!=-1 && zero<1){
            out[index]=prod;
            return out;
        }
        else if(zero>=1){
            return out;
        }
        for(int i = 0; i<nums.length; i++){
            int temp;
            if(set.get(i)==0) temp = 0;
            else temp = prod/set.get(i);
            out[i]=temp;
        }
        return out;
    }
}