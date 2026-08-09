import java.util.*;

class Solution {
    static int N, answer;
    static String str;
    static boolean[] v;
    static Set<Integer> set = new HashSet<>();
    
    static boolean checkPrime(String num) {
        int n = Integer.parseInt(num);
        if (set.contains(n) || n==0 || n==1) {
            return false;
        }
        set.add(n);
        // System.out.println(set);
        
        for (int i=2; i<n; i++) {
            if (n%i == 0) {
                return false;
            }
        }
        return true;
    }
    
    static void dfs(String num) {
        if (!num.equals("") && checkPrime(num)) {
            answer += 1;
        }
        
        if (num.length() == N) {
            return;
        }
        
        for (int i=0; i<N; i++) {
            if (v[i]) {
                continue;
            }
            
            num += str.charAt(i);
            v[i] = true;
            // System.out.println("-----before dfs-----");
            // System.out.println(num);
            // System.out.println(v[0] +" "+ v[1]);
            dfs(num);
            num = num.substring(0, num.length()-1);
            v[i] = false;
            // System.out.println("-----after dfs-----");
            // System.out.println(num);
            // System.out.println(v[0] +" "+ v[1]);
                
        }
        
    }
    
    
    public int solution(String numbers) {
        answer = 0;
        N = numbers.length();
        v = new boolean[N];
        str = numbers;
        
        dfs("");
        
        return answer;
    }
}