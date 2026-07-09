class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        if(nums.length<3) return list;
        Arrays.sort(nums);
        for(int i = 0; i<nums.length-2; i++){
            //System.out.println(i);
            int j = i+1;
            int k = nums.length-1;
            while(j<k){
                int sum = nums[i]+nums[j]+nums[k];
                if(sum>0){
                    k--;
                    continue;
                }
                else if(sum<0){
                    j++;
                    continue;
                }
                else{
                    List<Integer> arr = new ArrayList<>();
                    arr.add(nums[i]);
                    arr.add(nums[j]);
                    arr.add(nums[k]);
                    if(!list.contains(arr)) list.add(arr);
                    j++;
                    k--;
                }
            }
        }
    return list;
    }
}

