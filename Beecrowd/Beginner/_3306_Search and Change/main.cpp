#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

int main() {
    int tam_vetor, n_queries;
    cin >> tam_vetor >> n_queries;
    
    vector<int> vetor(tam_vetor);
    for (int i = 0; i < tam_vetor; i++) {
        cin >> vetor[i];
    }
    
    for (int i = 1; i <= n_queries; i++) {
        vector<int> query;
        int val;
        while (cin >> val) {
            query.push_back(val);
            if (cin.peek() == '\n' || cin.eof()) break;
        }
        
        if (query.size() < 3) {
            cout << i << endl;
        } else if (query[0] == 1) {
            for (int c = query[1] - 1; c < query[2]; c++) {
                vetor[c] += query[3];
            }
        } else {
            int result = vetor[query[1] - 1];
            for (int c = query[1]; c < query[2]; c++) {
                result = __gcd(result, vetor[c]);
            }
            cout << result << endl;
        }
    }
    return 0;
}
