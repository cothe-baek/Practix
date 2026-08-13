import java.util.*;

class Solution {
    Set<String> set = new HashSet<>();
    
    public boolean solution(String[] phone_book) {
        
        for (String str : phone_book) {
            set.add(str);
        }
        
        for (String str : set) {
            for (int i=1; i<str.length(); i++) {
                String head = str.substring(0, i);
                if (set.contains(head)) {
                    return false;
                }
            }
            
        }
        
        return true;
    }
}