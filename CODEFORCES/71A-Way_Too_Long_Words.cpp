#include <iostream>
#include <string>
using namespace std;

int main(){
    int n;
    cin >> n;
    string arr[n];
    for(int i = 0; i < n; i ++){
        cin >> arr[i];
    }
    for(int i = 0;i < n;i++){
        if (arr[i].length() > 10){
            cout << arr[i].substr(0,1) << arr[i].length() - 2 << arr[i].substr(arr[i].length()-1,1) << "\n";
        }
        else {
            cout << arr[i] << "\n";
        }
    }
}