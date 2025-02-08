#include <bits/stdc++.h>

using namespace std;

int main(){
    int P,N; cin >> P>>N;
    vector<int> vet(N);
    for (int i = 0; i < N; ++i) {
        cin >> vet[i];
    }
    
    for (int i = 1;i<N;i++){
        if (P < abs(vet[i]-vet[i-1])){
            cout << "GAME OVER" << endl;
            return 0;

        }
    }
    cout << "YOU WIN" << endl;
    return 0;
}