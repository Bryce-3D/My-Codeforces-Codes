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

*/

/* DEBUG LOG

*/

// Comment this out to turn off debugging
// #define DEBUG


void solve() {
    int n,k;
    cin >> n >> k;

    // n-k to n then n-k-1 to 1
    for (int i = n-k; i <= n; i++) {
        cout << i << " ";
    }
    for (int i = n-k-1; i >= 1; i--) {
        cout << i << " ";
    }
    cout << endl;
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
