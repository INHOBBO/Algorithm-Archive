class Solution {
    public int[] solution(int money) {
        int[] answer = new int[2];
        int iced = 5500;
        // 거스름돈 = money % 5500
        int exchange = money % iced;
        answer[0] = money / iced;
        answer[1] = exchange;
        return answer;
    }
}