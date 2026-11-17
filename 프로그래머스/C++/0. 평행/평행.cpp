#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> dots) {
    int answer = 0;
    
    auto is_parallel = [&] (int a, int b, int c, int d) {
        int dx1 = dots[a][0] - dots[b][0];
        int dx2 = dots[c][0] - dots[d][0];
        int dy1 = dots[a][1] - dots[b][1];
        int dy2 = dots[c][1] - dots[d][1];
        
        return dx1 * dy2 == dx2 * dy1;
    };
    
    if (is_parallel(0, 1, 2, 3) || is_parallel(0, 2, 1, 3) || is_parallel(0, 3, 2, 1)) {
        return true;
    }
    return false;
}