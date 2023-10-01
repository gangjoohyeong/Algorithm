class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        char[] charArr = s.toCharArray();
        for(char word: charArr) {
            if (word == 'p' || word == 'P') {
                p += 1;
            } else if (word == 'y' || word =='Y') {
                y += 1;
            }
        }
        if (p == y) {
            return true;
        } else {
            return false;
        }
    }
}