class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(String i : strs){
            char[] arr = i.toCharArray();
            Arrays.sort(arr);
            String s = new String(arr);
            if(map.containsKey(s)){
                map.get(s).add(i);
            }else{
                List<String> list = new ArrayList<>();
                list.add(i);
                map.put(s, list);
            } 
        }
        return new ArrayList<>(map.values());
    }
}
