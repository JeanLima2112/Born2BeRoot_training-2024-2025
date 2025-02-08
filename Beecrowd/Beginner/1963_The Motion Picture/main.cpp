#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

int main(){
    double X,Y; cin >> X >> Y;
    cout << fixed << setprecision(2);
    cout << ((Y*100)/X) -100 <<"%"<<endl;
}