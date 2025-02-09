#include <bits/stdc++.h>

using namespace std;

int main(){
    int S,T,F; cin >>S>>T>>F;
    int result = S+T+F;
    if (result>= 24){
        cout << result-24 <<endl;

    }else if(result < 0){
        cout <<24 + result  <<endl;
    
    }else if(result >= 0){
        cout << result  <<endl;
    }
    else{
        cout <<24 - result  <<endl;
    }
    return 0;
}
