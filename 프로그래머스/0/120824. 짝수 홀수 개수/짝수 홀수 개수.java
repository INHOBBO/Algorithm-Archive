class Solution {
    // 짝수는 answer[0], 홀수는 answer[1]
    public int[] solution(int[] num_list) {
        int[] answer = {0,0};
        
        for (int i=0;i<num_list.length;i++) {
            if (num_list[i] % 2 == 0) { // 짝수일 경우
                answer[0] += 1;
            } else {
                answer[1] += 1;
            }
        }
        
        return answer;
    }
}