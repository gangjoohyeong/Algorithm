import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {;
        String[] sArray = s.split("");
        Arrays.sort(sArray, Collections.reverseOrder());
        return String.join("", sArray);
    }
}