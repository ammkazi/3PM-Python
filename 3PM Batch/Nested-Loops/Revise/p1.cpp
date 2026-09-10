#include <iostream>
using namespace std;

void changeValue(int &x)
{
    x = x + 10;
    cout << "Value of num inside fn is " << x << endl;
}

int main()
{
    int num = 20;
    cout << "Value of num before fn call is " << num << endl;
    changeValue(num);
    cout << "Value of num after fn call is " << num << endl;
}