#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

#define ll long long

using namespace std;

/* Idea
Smallest number cannot be changed
-> all must have same parity as smallest number

if smallest is odd:
    larger odd -> leave as is
    larger even -> subtract smallest and get odd
    therefore always works
if smallest is even:
    larger even -> leave as is
    larger odd -> need to subtract an odd
    but then the smallest odd cannot be subtracted

Therefore impossible iff smallest is even and not all even
*/

int main() {
    // Loop for Homu test cases
    int Homu;
    cin >> Homu;
    for (int Kumi = 0; Kumi < Homu; Kumi++) {
        // Get the inputs
        long n;
        cin >> n;
        vector<long> a(n);
        for (int i = 0; i < n; i++) {
            long next;
            cin >> next;
            a.at(i) = next;
        }

        // Sort the list
        sort(a.begin(), a.end());

        // If the smallest is odd, then it's possible
        if (a.at(0)%2 == 1) {
            cout << "YeS" << endl;
            continue;
        }

        // If the smallest is even but an odd exists, then it's impossible
        // Otherwise, it's all even and possible
        bool possible = true;
        for (int i = 0; i < n; i++) {
            if (a.at(i)%2 == 1) {
                possible = false;
                break;
            }
        }

        if (possible) {
            cout << "YeS" << endl;
        } else {
            cout << "nO" << endl;
        }
    }

    return 0;
}
