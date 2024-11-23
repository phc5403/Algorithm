import java.util.*;

class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        
        int center = total / num;
        int start = center - (num - 1) / 2;
        
        System.out.printf("%d %d", center, start);
        
        for (int i = 0; i < num; i++) {
            answer[i] = start + i;
        }
        
        System.out.println(Arrays.toString(answer));
        
        return answer;
    }
}