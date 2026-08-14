import java.util.*;

class Solution {
    Map<String, List<String>> map = new HashMap<>();
    
    
    public int solution(String[][] clothes) {
        int answer = 1;
        
        for (String[] row : clothes) {
            if (!map.containsKey(row[1])) {
                map.put(row[1], new ArrayList<>());
            }
            map.get(row[1]).add(row[0]);
        }
        
        int totalCnt = 0;
        List<Integer> lst = new ArrayList<>();
        
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            String key = entry.getKey();
            List<String> val = entry.getValue();
            
            System.out.println(val);
            int tmpCnt = val.size();
            lst.add(tmpCnt);
        }
        
        for (int i : lst) {
            answer *= (i+1);
        }
        
        return answer-1;
    }
}