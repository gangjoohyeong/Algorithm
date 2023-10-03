import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 45;
        int[] newNumbers = Arrays.stream(numbers).distinct().toArray();
        for (int num : newNumbers) {
            answer -= num;
        }
        return answer;
    }
}
