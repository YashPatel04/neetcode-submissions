class Solution {
    public int trap(int[] h) {
        int sum = 0;
        int n = h.length-1;
        List<Integer> fwdMax = new ArrayList<>();
        List<Integer> bwdMax = new ArrayList<>();
        int max = 0;
        for(int i: h){
            if(i>max) max = i;
            fwdMax.add(max);
        }
        max = 0;
        for(int i=h.length-1; i>=0; i--){
            if(h[i]>max) max = h[i];
            bwdMax.add(max);
        }
        Collections.reverse(bwdMax);
        for(int i=0; i<h.length-1; i++){
            sum += Math.min(fwdMax.get(i), bwdMax.get(i)) - h[i];
        }
        return sum;
    }
}