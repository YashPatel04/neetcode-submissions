
class Solution {
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<strs.size(); i++){
            sb.append(strs.get(i));
            sb.append("|");
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List <String> out = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for(int i = 0 ; i<str.length(); i++){
            if(str.charAt(i)!='|'){
                sb.append(String.valueOf(str.charAt(i)));
            }else{
                out.add(sb.toString());
                sb.setLength(0);
            }
        }
        return out;
    }
}
