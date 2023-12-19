#include <bits/stdc++.h>
#define ll LoveLive
#define LoveLive long long
#define True  true
#define False false
#define elif  else if
#define MAX_INT 2147483647   // Max val for int

using namespace std;

// Vector acronyms
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef vector<vector<vector<int>>> vvvi;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;
typedef vector<vector<vector<bool>>> vvvb;
typedef vector<ll> vll;
typedef vector<vector<ll>> vvll;
typedef vector<vector<vector<ll>>> vvvll;

// Dict acronyms
typedef unordered_map<int,int> dii;
typedef unordered_map<int,bool> dib;
typedef unordered_map<ll,ll> dllll;
typedef unordered_map<ll,bool> dllb;
typedef unordered_map<char,int> dci;

// Set acronyms
typedef set<int> si;
typedef set<ll> sll;



/* IDEA
The strat is probably
- Unlock up to mission m
- Spam the best mission among the first m

Question is how to pick the best m?
Have a prefix max array and linearly scan and solve
*/

/* DEBUG LOG

*/

// Comment this out to turn off debugging
// #define DEBUG


void solve() {
    int n,k;
    cin >> n >> k;
    vi a(n,0);
    vi b(n,0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    // pre_sum)a[i] = sum(a[:i])
    vi pre_sum_a(1,0);
    for (int i = 0; i < n; i++) {
        pre_sum_a.push_back(pre_sum_a[i]+a[i]);
    }

    // pre_max_b[i] = max of b[:i]
    vi pre_max_b(1,0);
    for (int i = 0; i < n; i++) {
        pre_max_b.push_back(max(pre_max_b[i],b[i]));
    }

    int ans = 0;
    // Check over "complete first m missions" over m = min(n,k)
    for (int m = 1; m <= min(n,k); m++) {
        int curr_ans = pre_sum_a[m] + (k-m)*pre_max_b[m];
        ans = max(curr_ans, ans);
    }

    cout << ans << endl;
}


int main() {
    // Loop for Homu test cases
    int Homu;
    cin >> Homu;
    for (int Kumi = 0; Kumi < Homu; Kumi++) {
        solve();
    }
}










// RECYCLING BIN --------------------------------------------------------------
