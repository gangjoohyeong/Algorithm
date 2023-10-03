class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            int[] answer = {-1};
            return answer;
        } else {
            int idx = 0;
            for (int i = 1; i < arr.length; i++) {
                if (arr[idx] > arr[i]) {
                    idx = i;
                }
            }
            int[] result = new int[arr.length - 1];
            for (int i = 0, j = 0; i < arr.length; i++) {
                if (i != idx) {
                    result[j] = arr[i];
                    j++;
                }
            }
            return result;
        }
    }
}
