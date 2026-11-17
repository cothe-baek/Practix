#include <string>
#include <vector>

using namespace std;

vector<int> solution(int num, int total) {
    vector<int> answer;
    
    for (int n = -50; n <= 1000; n++) {
        int base = n * num;
        int adds = num * (num-1) / 2;
        int tmp = base + adds;
        
        if (tmp == total) {
            for (int x = 0; x < num; x++) {
                answer.push_back(n+x);
            }
            break;
        }
    }
    return answer;
}