import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> newList = new ArrayList<Integer>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % divisor == 0) {
                newList.add(arr[i]);
            }
        }
        
        if (newList.size() == 0) {
            newList.add(-1);   
        }
        
        int[] result = new int[newList.size()];
        for (int i = 0; i < newList.size(); i++) {
            result[i] = newList.get(i);
        }
        
        Arrays.sort(result);
        return result;
    }
}