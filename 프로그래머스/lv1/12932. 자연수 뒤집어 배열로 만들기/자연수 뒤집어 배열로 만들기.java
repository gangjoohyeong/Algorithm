class Solution {
    public int[] solution(long n) {
        String nString = Long.toString(n);
        int[] arr = new int[nString.length()];
        
        for (int i = 0; i < nString.length(); i++) {
            arr[nString.length() - i - 1] = Integer.parseInt(String.valueOf(nString.charAt(i)));
        }
        
        return arr;
    }
}
