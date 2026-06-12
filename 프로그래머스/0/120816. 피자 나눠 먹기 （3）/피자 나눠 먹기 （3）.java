class Solution {
    // n나누기slice 해서 나머지가 0이면 그대로, 나머지 0아니면 +1
    public int solution(int slice, int n) {
        int answer = 0;
        
        if (n % slice == 0) {
            answer = n / slice;
        } else {
            answer = n / slice + 1;
        }
        
        return answer;
    }
}