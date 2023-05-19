#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main() {
    int Homu;
    cin >> Homu;
    for (int Kumi = 0; Kumi < Homu; Kumi++) {
        int n;
        string s;
        cin >> n >> s;

        set<string> seen;
        for (int i = 0; i < n-1; i++) {
            string sub = s.substr(i,2);
            seen.insert(sub);
        }

        cout << seen.size() << endl;
    }

    return 0;
}
