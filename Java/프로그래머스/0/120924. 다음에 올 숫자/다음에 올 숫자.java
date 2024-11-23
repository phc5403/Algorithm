import java.util.*;

class Solution {
    public int solution(int[] common) {
        int answer = 0;
        
        // 1. 등차수열 일 경우
        if(common[2] - common[1] == common[1] - common[0]) {
            answer = common[common.length - 1] + (common[1] - common[0]);
        }
        else { // 2. 등비수열 일 경우
            answer = common[common.length - 1] * (common[1] / common[0]);
        } 

        
        return answer;
    }
}