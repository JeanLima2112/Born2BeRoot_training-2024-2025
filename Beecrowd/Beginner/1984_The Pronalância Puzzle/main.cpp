#include <bits/stdc++.h>

using namespace std;

int main(){

    char number[11] = "";
    cin >> number;
    size_t size = strlen(number);
    for (int i = 0; i<size/2;i++){
        char tpm = number[i];
        number[i] = number[size-1-i];
        number[size -i -1]=tpm;
    }
    cout << number << endl;
    

    return 0;
}