class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if (a < b) {
            answer += (long) b * (b+1) / 2;
            answer -= (long) a * (a-1) / 2;
        } else {
            answer += (long) a * (a+1) / 2;
            answer -= (long) b * (b-1) / 2;
        }
        
        return answer;
    }
}


