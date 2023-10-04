class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long usingMoney = 0;
        
        for(int i = 0; i < count; i++) {
            usingMoney += price * (i+1);
        }
        if (usingMoney - money < 0) {
            return 0;
        } else {
            return usingMoney - money;
        }   
    }
}