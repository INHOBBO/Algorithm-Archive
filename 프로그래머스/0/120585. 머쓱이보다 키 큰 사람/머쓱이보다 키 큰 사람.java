class Solution {
    // height값보다 큰 값이 array 배열에 몇개가 있니?
    public int solution(int[] array, int height) {
        int answer = 0;
        
        for (int i=0; i<array.length; i++) {
            if (array[i] > height) {
                answer += 1;
            }
        }
        
        return answer;
    }
}