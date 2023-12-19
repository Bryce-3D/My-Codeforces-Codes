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
Change to 0-indexing
Everyone is under 0 -> it is a tree rooted at 0

Pairs impossible iff remaining part is a line graph/total order
Greedily pair up 2 leaves with max depth?



Idea for F you most probably just keep greedily picking 2 leaves at the lowest level
Question: How the fuck do you implement this/count without implementing this
:HomuraThink~1:
Cannot braindead BFS
I can troll and play bandori instead of doing this for a bit
:trolley:
actually wait
pq of leaves
?
pq contains leaves, priority = their depth
I forgor if c++ pq was min or max
tonikaku can negate if needed
uh
removing a leaf may reveal at most one new leaf (the parent)
how check this?
perhaps keep "number of children" counter
if this hits 0 = congrats your bloodline is dead and you are now a leaf
then toss into pq
only toss into pq after removing a pair not after each
question
how find number of children
wait that's trivial it's literally just do while building tree
how will I store tree
what do I need
mmmmmm
why is implementing graphs pain
uh
par[i] = parent of i as usual ig?
par[0] = -1
I also need depth
depth[i] = depth of node i
set depth[0] = 0
then how
ig create edges pointing downwards then BFS?
somewhat
then BFS does it per lvl
do can always do
depth[i] = depth[par[i]] + 1
wait I am using C++™️ not Python™️
ok surely can't be that bad
uh then what
that gives depth
right I need number of children
I can reconstruct from this (ig create edges pointing downwards then BFS?)
n_child[i] = number of alive children of i
wAIT is there a corner case
suppose you have a tie for leaf depth
say 3
how know which 2 to pair
is there a scenario
you pair 2 of them better than some other pair
all common parent -> doesn't matter
all diff parent -> doesn't matter
2-1 split -> uh
also doesn't matter
say 4 -> all paired
say 2k on same lvl -> all paired
say 2k+1 on same lvl
1 trivial case
it just that
3 alr good
how 5
can it matter
ok in general
suppose 2k+1 leaves at depth d (current lowest depth)
you nuke them with k pairs
1 left
how can the position of this last 1 affect the rest of the shit
it must be attached to something at depth k
everything else at depth k should now be a leaf
oh ok good it literally doesn't matter
very nice
so just throw into pq = prio for some is fine
par[i]   = parent of node `i`   #Given
depth[i] = depth of node `i`    #Need to BFS
n_chi[i] = number of undead children of node `i`   
    #Just count while building `par`? Then update every pair we make
Is that all
I also need a pq
iirc C++ does have a PQ right
how much time
41 mins surely I can do this in 40 mins
ok
*/

/* DEBUG LOG

*/

// Comment this out to turn off debugging
// #define DEBUG


void solve() {
    int n;
    cin >> n;

    // par[i] = parent of node `i`
    vi par(n,-1);
    // chi[i] = list of children of node `i`
    vvi chi(n, vi(0));
    // depth[i] = depth of node `i`
    vi depth(n,0);

    for (int u = 1; u < n; u++) {
        cin >> par[u];
        par[u] -= 1;   // 0-index this
        chi[par[u]].push_back(u);
    }

    // BFS to build the depth
    vi BFS{0};   // Nodes in BFS order
    for (int v : chi[0]) {
        BFS.push_back(v);
    }
    for (int i = 1; i < n; i++) {
        int v = BFS[i];
        depth[v] = depth[par[v]] + 1;   // Record depth
        // Put children into BFS "queue"
        for (int v_chi : chi[v]) {
            BFS.push_back(v_chi);
        }
    }

    // n_chi[i] = number of unpaired children of node `i`
    vi n_chi(n);
    for (int i = 0; i < n; i++) {
        n_chi[i] = chi[i].size();
    }
    // pq of leaves to pair up
    // Each element is of the form [depth, index]
    priority_queue<vi> pq;
    for (int i = 0; i < n; i++) {
        if (n_chi[i] == 0) {
            pq.push(vi{depth[i],i});
        }
    }

    int ans = 0;
    while (pq.size() >= 2) {
        int l0 = pq.top()[1];   // Leaf 0
        pq.pop();
        int l1 = pq.top()[1];   // Leaf 1
        pq.pop();

        int p0 = par[l0];   // Parent of leaf 0
        int p1 = par[l1];   // Parent of leaf 1

        // Update parent's number of children of their parents and toss into 
        // pq if it becomes 0. Corner case of p0=p1 is fine since the check is 
        // done after each decrement rather than after both
        n_chi[p0] -= 1;
        if (n_chi[p0] == 0) {
            pq.push(vi{depth[p0],p0});
        }
        n_chi[p1] -= 1;
        if (n_chi[p1] == 0) {
            pq.push(vi{depth[p1],p1});
        }

        // Have another pair
        ans += 1;
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
