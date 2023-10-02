class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        char[] arr = Integer.toString(x).toCharArray();
        int tmp = 0;
        for(char value: arr) {
            int n = Character.getNumericValue(value);
            tmp += n;
        }
        if (x % tmp == 0) {
            return true;
        } else {
            return false;
        }
    }
}