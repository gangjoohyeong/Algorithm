import java.util.*;

public class Solution {
    public Integer[] solution(int[] arr) {
        List<Integer> list = new ArrayList<Integer>();
        int now = arr[0];
        list.add(now);
        for (int a : arr) {
            if (a != now) {
                list.add(a);
                now = a;
            }
        }
        Integer[] answer = new Integer[list.size()];
        return list.toArray(answer);
    }
}
