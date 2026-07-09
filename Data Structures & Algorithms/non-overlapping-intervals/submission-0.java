class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if(intervals.length == 1) return 0;
        int left = 0;
        int right = intervals.length-1;
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        int currStart = 0;
        int prevEnd = 0;
        int count = 0;
        for(int i = 0; i<intervals.length; i++){
            if(i==0){
                prevEnd = intervals[0][1];
                continue;
            }
            currStart = intervals[i][0];
            if(prevEnd<=currStart){
                prevEnd = intervals[i][1];
            }else{
                count++;
            }
        }
        return count;
    }
}