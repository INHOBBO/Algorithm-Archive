class Solution {
    // 양꼬치 10인분 먹으면 음료수 하나 서비스
    public int solution(int n, int k) {
        int answer = 0;
        answer = n*12000 + k*2000 - n/10*2000;
        return answer;
    }
}