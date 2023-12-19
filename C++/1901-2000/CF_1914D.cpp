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
ONLY LARGEST 3 NUMBERS OF EACH ARRAY IS RELEVANT
Store the largest 3 of each array
Manually bash each of the at most 3^3=27 ways to do it

WAIT I NEED TO HANDLE TIES FUCK
Ok just store all the days ig that works too
Or rather store at most 3 days
Maybe I can just make it go up to 5 then, so that ties will be handled
*/

/* DEBUG LOG

*/

// Comment this out to turn off debugging
// #define DEBUG


void solve() {
    int n;
    cin >> n;

    vi a(n), b(n), c(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }

    // Corner case
    if (n < 5) {
        int ans = 0;
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                for (int z = 0; z < n; z++) {
                    if (x==y || y==z || z==x) {
                        continue;
                    }
                    ans = max(a[x]+b[y]+c[z], ans);
                }
            }
        }
        cout << ans << endl;
        return;
    }

    vvi top_a(5), top_b(5), top_c(5);
    for (int i = 0; i < 5; i++) {
        top_a[i] = vi{a[i],i};
        top_b[i] = vi{b[i],i};
        top_c[i] = vi{c[i],i};
    }
    sort(top_a.begin(),top_a.end());
    sort(top_b.begin(),top_b.end());
    sort(top_c.begin(),top_c.end());

    for (int i = 5; i < n; i++) {
        if (a[i] > top_a[0][0]) {
            top_a[0] = vi{a[i],i};
            sort(top_a.begin(),top_a.end());
        }
        if (b[i] > top_b[0][0]) {
            top_b[0] = vi{b[i],i};
            sort(top_b.begin(),top_b.end());
        }
        if (c[i] > top_c[0][0]) {
            top_c[0] = vi{c[i],i};
            sort(top_c.begin(),top_c.end());
        }
    }

    int ans = 0;
    for (int x = 0; x < 5; x++) {
        for (int y = 0; y < 5; y++) {
            for (int z = 0; z < 5; z++) {
                // 3 days must be distinct
                int d_x = top_a[x][1];
                int d_y = top_b[y][1];
                int d_z = top_c[z][1];
                if (d_x == d_y || d_y == d_z || d_z == d_x) {
                    continue;
                }
                // If all distinct, update ans if needed
                int n_x = top_a[x][0];
                int n_y = top_b[y][0];
                int n_z = top_c[z][0];
                ans = max(n_x+n_y+n_z, ans);
            }
        }
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
