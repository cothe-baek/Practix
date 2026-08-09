import java.util.*;

class Solution {
    // [개선 1] 변수 선언
    // 기존: static 전역 변수로 인해 여러 테스트 케이스 실행 시 이전 데이터가 남아 오답 발생 가능성 존재
    // 나중 실무를 위해서라도 static은 자제합시다
    
    // 변경: 인스턴스 변수로 변경하여 매 solution() 호출 시마다 새롭게 초기화되도록 수정
    int N, answer;
    String str;
    boolean[] v;
    Set<Integer> set;
    
    // [개선 2] 소수 판별 로직 (성능 최적화)
    // 기존: static boolean checkPrime(String num) { ... }
    // 변경: 매개변수를 int로 받고, 제곱근까지만 검사하여 시간 복잡도를 크게 단축
    boolean checkPrime(int n) {
        // 기존:
        // int n = Integer.parseInt(num);
        // if (set.contains(n) || n==0 || n==1) { return false; }
        // set.add(n);
        
        if (n == 0 || n == 1) {
            return false;
        }
        
        // 기존: for (int i=2; i<n; i++) { ... }
        // 변경: 약수는 대칭을 이루므로 Math.sqrt(n)까지만 검사해도 충분함
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    // [개선 3] DFS 백트래킹 로직 (가독성 및 구조 개선)
    // 기존: static void dfs(String num)
    void dfs(String num) {
        // 기존: 중복 검사도 checkPrime 안에서 수행
        // if (!num.equals("") && checkPrime(num)) {
        //     answer += 1;
        // }
        
        // 변경: Set을 이용한 중복 검사와 소수 판별 책임을 명확히 분리
        if (!num.equals("")) {
            int n = Integer.parseInt(num);
            if (!set.contains(n)) {
                set.add(n); // 여기서 중복 차단
                if (checkPrime(n)) {
                    answer++;
                }
            }
        }
        
        if (num.length() == N) {
            return;
        }
        
        for (int i = 0; i < N; i++) {
            if (v[i]) {
                continue;
            }
            
            // 기존: 문자열을 직접 수정하고 substring으로 복원하는 방식
            // num += str.charAt(i);
            // v[i] = true;
            // dfs(num);
            // num = num.substring(0, num.length()-1);
            // v[i] = false;
            
            // 변경: 다음 재귀 함수로 넘어갈 때 인자에서만 문자열을 더해줌
            // 이렇게 하면 현재 스코프의 num은 변하지 않으므로 substring 복원 과정이 아예 필요 없음.
            v[i] = true;
            dfs(num + str.charAt(i)); 
            v[i] = false;
            
            // 혹은 StringBuilder로 처리하면서
            // .append(str.charAt(i))와 .deleteCharAt(idx) 활용도 가능
            // 대신 이건 parseInt할 때 toString 해주고 해야함
        }
    }
    
    public int solution(String numbers) {
        
        // 변경: Set 컬렉션도 solution 내부에서 명시적으로 새로 생성하여 안전성 확보
        answer = 0;
        N = numbers.length();
        v = new boolean[N];
        str = numbers;
        set = new HashSet<>();
        
        dfs("");
        
        return answer;
    }
}
