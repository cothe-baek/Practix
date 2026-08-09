import java.util.*;

class Solution {
    int[][] arr;
    
    void markEdge() {
        int N = arr.length; int M = arr[0].length;
        int[] cur;
        int[] di = {-1, 1, 0, 0, -1, 1, 1, -1};
        int[] dj = {0, 0, -1, 1, -1, 1, -1, 1};
        int ci, cj, ni, nj;
        
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] v = new boolean[N][M];
        
        q.add(new int[] {0, 0});
        v[0][0] = true;
        
        while(!q.isEmpty()) {
            cur = q.poll();
            ci = cur[0]; cj = cur[1];
            
            for (int d=0; d<8; d++) {
                ni = ci + di[d]; nj = cj + dj[d];
                
                if (0<=ni && ni<N && 0<=nj && nj<M && !v[ni][nj]) {
                    if (arr[ni][nj] > 0) {
                        arr[ni][nj] = 2;
                    }
                    else {
                        q.add(new int[] {ni, nj});
                    }
                    v[ni][nj] = true;
                }
            }
        }  
    }
    
    int bfs(int i, int j, int ei, int ej) {
        int N = arr.length; int M = arr[0].length;
        int[] cur;
        int[] di = {-1, 1, 0, 0};
        int[] dj = {0, 0, -1, 1};
        int ci, cj, cm, ni, nj, nm;
        int minMove = 10000;
        
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] v = new boolean[N][M];
        
        q.add(new int[] {i, j, 0});
        v[i][j] = true;
        
        while(!q.isEmpty()) {
            cur = q.poll();
            ci = cur[0]; cj = cur[1]; cm = cur[2];
            
            for (int d=0; d<4; d++) {
                ni = ci + di[d]; nj = cj + dj[d]; nm = cm + 1;
                
                if (0<=ni && ni<N && 0<=nj && nj<M && arr[ni][nj] == 2 && !v[ni][nj]) {
                    // 도착지라면 방문처리는 하지 말고 (다른 방향에서도 한번 더 와야 함) 길이만
                    if (ni == ei && nj == ej) {
                        minMove = Math.min(minMove, nm);
                    }
                    else {
                        q.add(new int[] {ni, nj, nm});
                        v[ni][nj] = true;
                    }
                }
            }
        }
        return minMove/2;
    }
    
    
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        int MAX_X = 0; int MAX_Y = 0;
        
        // get max x & y to draw 2 times scaled 2D coordinate
        for (int[] r : rectangle) {
            MAX_X = Math.max(MAX_X, r[2]*2);
            MAX_Y = Math.max(MAX_Y, r[3]*2);
        }
        
        // 2 times scaled 2D coordinate
        arr = new int[MAX_X+2][MAX_Y+2];
        
        // draw rectangles on arr
        for (int[] r : rectangle) {
            for (int x = r[0]*2; x <= r[2]*2; x++) {
                for (int y = r[1]*2; y <= r[3]*2; y++) {
                    arr[x][y] = 1;
                }
            }
        }
        
        // mark edge lines of arr with number 2
        markEdge();
        
        
        // for (int[] row : arr) {
        //     for (int val : row) {
        //         System.out.printf("%2d ", val);
        //     }
        //     System.out.println();
        // }
        // System.out.println();
        
        answer = bfs(characterX*2, characterY*2, itemX*2, itemY*2);
        
        return answer;
    }
}