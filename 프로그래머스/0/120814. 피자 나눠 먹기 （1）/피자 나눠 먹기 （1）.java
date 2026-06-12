// 피자를 7조각
// 나누고 올림 하는게 맞는데

class Solution {
    public int solution(int n) {
        double answer = 0;
        answer = (double) n / 7;
        return (int) Math.ceil(answer);
    }
}