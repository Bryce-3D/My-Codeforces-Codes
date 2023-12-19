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
So essentially at each turn, a color is nuked
Suppose A nukes color i
Then A will have a_i-1 pts while B has 0 pts from this color
We can instead treat it as a = [i-1 for i in a] and similar for b
And each turn is claiming a color and getting the corresponding number 
of points as indicated by a or b resp.

Consider a pair (a_i,b_i)
A picking a_i -> score += a_i
B picking b_i -> score -= b_i
Whether or not A or B picks this color causes a net diff of a_i+b_i
THEREFORE THE COLORS WITH A LARGER SUM ARE MORE IMPORTANT

Question now is how to impl
We can ig

sum of a,b
append index
sort this
linearly scan back to get the final score
*/

/* DEBUG LOG

*/

// Comment this out to turn off debugging
// #define DEBUG


void solve() {
    int n;
    cin >> n;

    vll a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        a[i] -= 1;
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
        b[i] -= 1;
    }
    
    // s contains terms of the form [-a[i]-b[i], i]
    // To be sorted according to negative of the sum so that larger 
    // totals appear in front instead
    vvll s(n, vll{0,0});
    for (int i = 0; i < n; i++) {
        s[i][0] = -a[i]-b[i];
        s[i][1] = i;
    }
    sort(s.begin(),s.end());

    ll ans = 0;
    for (int i = 0; i < n; i++) {
        int ind = s[i][1];
        if (i%2 == 0) {
            ans += a[ind];
        } else {
            ans -= b[ind];
        }
    }
    cout << ans << endl;



    #ifdef DEBUG
    for (vll v : s) {
        for (ll i : v) {
            cout << i << " ";
        }
        cout << endl;
    }
    cout << endl << endl;
    #endif
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
