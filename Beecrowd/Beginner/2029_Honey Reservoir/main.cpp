#include <bits/stdc++.h>

using namespace std;

int main(){
    double V,D;
    double raio, area;

    cout << fixed << setprecision(2);
    
    while(cin >> V >> D){
        raio = D /2;
        area = 3.14 * (raio *raio);
        cout << "ALTURA = "<<V / area << endl;
        cout << "AREA = "<< area << endl;


    }
    
    return 0;
}
