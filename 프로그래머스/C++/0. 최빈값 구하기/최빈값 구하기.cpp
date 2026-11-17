#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    int mx_freq = 0;
    
    map<int, int> counts;
    
    for (int x: array) {
        counts[x]++;
    }
    
    for (auto p: counts) {
        int key = p.first;
        int freq = p.second;
        
        if (freq > mx_freq) {
            answer = key;
            mx_freq = freq;
        }
        else if (freq == mx_freq) {
            answer = -1;
        }
    }
    
    return answer;
}