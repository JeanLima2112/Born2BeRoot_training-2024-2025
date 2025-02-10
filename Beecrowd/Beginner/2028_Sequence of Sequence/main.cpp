#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

int main()
{
    int X;
    int cont = 1;
    while (cin >> X){
        string out;
        if (X == 0){
            out = " numero";
        }else{
            out = " numeros";
        }
        int quant = 1;
        for (int i = X; i >= 0; i--)
        {
            quant += i;
        }
        cout << "Caso " << cont << ": " << quant <<out<< endl;
        cout << "0";
        for (int i = 1; i < X + 1; i++)
        {
            for (int j = 0; j < i; j++)
            {
                cout << " " << i;
            }
        }
        cont += 1;
        cout << endl<<endl;
        
    }

    return 0;
}
