#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

#define ll long long

using namespace std;

/* Idea
If you sort both lists, then they should match
You can greedy alg lowest with lowest
*/

struct Mahiro {
    long temp=0;
    long ind=0;

    // Constructors
    Mahiro() {
        this->temp = 0;
        this->ind = 0;
    }

    Mahiro(long t, long i) {
        this->temp = t;
        this->ind = i;
    }
};
// Define < operator so that I can use sort
bool operator < (const Mahiro& a, const Mahiro& b) {
    return a.temp < b.temp;
}

int main() {
    int Homu;
    cin >> Homu;
    for (int Kumi = 0; Kumi < Homu; Kumi++) {
        long n,k;
        cin >> n >> k;

        // To store the next element
        long next;

        // Get vector a with indices stored
        vector<Mahiro> a(n);
        for (long i = 0; i < n; i++) {
            cin >> next;
            a.at(i) = Mahiro(next,i);
        }

        // Get vector b
        vector<long> b(n);
        for (long i = 0; i < n; i++) {
            cin >> next;
            b.at(i) = next;
        }

        // Sort both a and b
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        // Create the answer vector
        vector<long> ans(n);
        for (long i = 0; i < n; i++) {
            // long pred_temp = a.at(i).temp;
            long true_temp = b.at(i);
            long ind = a.at(i).ind;

            ans.at(ind) = true_temp;
        }

        // Print the answer vector
        for (long i = 0; i < n; i++) {
            cout << ans.at(i) << ' ';
        }
        cout << endl;
    }

    return 0;
}
