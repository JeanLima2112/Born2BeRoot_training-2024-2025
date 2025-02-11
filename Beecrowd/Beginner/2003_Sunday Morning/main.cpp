#include <bits/stdc++.h>
#include <sstream>

using namespace std;

int main() {
    string time;
    int hours, minutes,total;
    char colon;
    while(cin >> time){
        stringstream ss(time);
        ss >> hours >> colon >> minutes;
        minutes += hours * 60;
        total = minutes - 480 + 60;

        if (total > 0){
            cout << "Atraso maximo: "<<total<<endl;
        } else{
            cout << "Atraso maximo: 0"<<endl;
        } 

    }
    
    return 0;
}
