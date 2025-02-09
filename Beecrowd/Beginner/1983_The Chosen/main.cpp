#include <bits/stdc++.h>

using namespace std;

int main(){
    string saida("Minimum note not reached");
    int N ; cin >> N;
    double Maior = 0 ;
    int X,ind;
    double Y;
    for(int i = 0; i<N;i++){
        cin >> X >> Y;
        if (Y > Maior){
            Maior = Y;
            ind = X ;
        }
    }
    if (Maior >= 8.0){
        cout<<ind<<endl;
    }else{
        cout << saida << endl;
    }
}