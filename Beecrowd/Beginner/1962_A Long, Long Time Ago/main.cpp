#include <bits/stdc++.h>

using namespace std;

int main(){
    int N; cin >> N;
    for (int i = 0; i<N;i++){
        int X; cin >> X;
        if(X >= 2015){
            cout << X - 2015 +1<<" A.C."<<endl;
        }
        else{
            cout << 2015 - X <<" D.C."<<endl;
        }
       
    }
    return 0;
}