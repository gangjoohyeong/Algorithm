class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int now = left; now <= right; now++) {
            int count = 0;
            for(int i = 1; i <= now; i++) {
                if(now % i == 0) {
                    count += 1;
                }
            }
            if (count % 2 == 0) {
                answer += now;
            } else {
                answer -= now;
            }
        }
        return answer;
    }
}