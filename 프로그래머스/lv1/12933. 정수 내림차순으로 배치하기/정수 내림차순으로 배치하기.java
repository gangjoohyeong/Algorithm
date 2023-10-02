import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n) {
        String tmp = "";
        
        String[] arr = Long.toString(n).split("");
        Arrays.sort(arr, Collections.reverseOrder());
        
        for(String s : arr) {
            tmp += s;
        }
        
        return Long.parseLong(tmp);
    } 
}