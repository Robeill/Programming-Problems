#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main(){
    string word;
    getline(cin,word);
    for (int i = 0; i < word.size();i++){
        word[i] = tolower(word[i]);
        if (word[i] != 'a' && word[i] != 'e' && word[i] != 'i' && word[i] != 'o' && word[i] != 'u' && word[i] != 'y'){
            cout << "." << word[i];
        }
    }
}
