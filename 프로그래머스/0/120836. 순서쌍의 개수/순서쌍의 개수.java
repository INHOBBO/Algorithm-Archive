class Solution {
    // 순서쌍 개수는 약수의 개수
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<=n; i++) {
            if (n % i ==0) {
                answer += 1;
            }
        }
        return answer;
    }
}