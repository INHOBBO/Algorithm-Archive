class Solution {
    public int[] solution(int n) {
        int[] answer = new int[(n+1)/2];
        
        int index = 0;
        // 1부터 n까지! 그런데, 홀수만
        for (int i=1; i<=n; i++) {
            if (i % 2 == 1) {
                answer[index] = i;
                index++;
            }
        }
        
        return answer;
    }
}