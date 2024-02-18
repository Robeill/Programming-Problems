#include <iostream>
#include <cctype>

using namespace std;

int main()
{
    string word;
    getline(cin, word);
    if (islower(word[0]))
    {
        word[0] = toupper(word[0]);
    }
    cout << word;
}