#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    int sum  = 0;
    for (int i = 0; i < n && m > 0; ++i) {
        if (v[i] < 0 && m > 0) {
            sum -= v[i];
            --m;
        } else if (v[i] >= 0) {
            break;
        }
    }
    cout << sum  << endl;
    return 0;
}
