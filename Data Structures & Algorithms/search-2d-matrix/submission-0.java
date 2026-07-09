class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int[] targArr = null;
        for (int[] i: matrix){
            if(i[0]<=target && i[i.length -1]>=target){
                targArr = i;
            }
        }
        if(targArr==null) return false;
        int start = 0;
        int end = targArr.length -1;
        while(start<=end){
            int mid = start + (end-start)/2;
            if(target>targArr[mid]){
                start = mid + 1;
            }
            else if(target < targArr[mid]){
                end = mid - 1;
            }else{
                return true;
            }
        }
        return false;
    }
}