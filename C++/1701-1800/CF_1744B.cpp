#include <iostream>
#include <vector>
#define ll long long
using namespace std;

int main() {
    int Homu;
    cin >> Homu;
    for (int Mado = 0; Mado < Homu; Mado++) {
        // Base inputs
        int n, q;
        cin >> n >> q;

        // Inputting a
        std::vector<int> a(n, 0);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        // Processing a
        int n_odd, n_even;
        ll s_odd, s_even;
        n_odd = 0;
        s_odd = 0;
        n_even = 0;
        s_even = 0;
        // for (auto i = a.begin(); i != a.end(); i++) {
        //     int next = *i;
        for(auto next: a) {
            if (next%2 == 0) {
                n_even += 1;
                s_even += next;
            } else {
                n_odd += 1;
                s_odd += next;
            }
        }

        for (int Kumi = 0; Kumi < q; Kumi++) {
            int type, x;
            cin >> type >> x;

            if (type == 0) {   // If add to evens
                s_even += n_even * x;   // Increase even total
                if (x%2 == 1) {         // If adding an odd number
                    s_odd += s_even;    // Move sum to odds
                    s_even = 0;
                    n_odd += n_even;    // Move count to odds
                    n_even = 0;
                }
            } else {   // If add to odds
                s_odd += n_odd * x;     // Increase odd total
                if (x%2 == 1) {         // If adding an odd number
                    s_even += s_odd;    // Move sum to evens
                    s_odd = 0;
                    n_even += n_odd;    // Move count to evens
                    n_odd = 0;
                }
            }

            cout << s_odd + s_even;   // Output the current total
            cout << '\n';             // New line between cases
        }
    }
}
