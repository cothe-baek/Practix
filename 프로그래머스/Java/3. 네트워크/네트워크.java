import java.util.*;

class Solution {
    static boolean[] v;
    
    static void bfs(int i, int n, int[][] arr) {
        Queue<Integer> q = new ArrayDeque<>();
        int ci, ni;
        
        q.add(i);
        v[i] = true;
        
        while (!q.isEmpty()) {
            ci = q.poll();
            
            for (ni=0; ni<n; ni++) {
                if (ni != ci && arr[ci][ni] == 1 && !v[ni]) {
                    q.add(ni);
                    v[ni] = true;
                }
            }
                
        }
    }
    
    public int solution(int n, int[][] computers) {
        v = new boolean[n];
        int answer = 0;
        
        for (int i=0; i<n; i++) {
            if (v[i]) {
                continue;
            }
            bfs(i, n, computers);
            answer++;
        }
        
        return answer;
    }
}