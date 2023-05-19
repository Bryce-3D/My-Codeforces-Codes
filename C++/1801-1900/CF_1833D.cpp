#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

#define ll long long

using namespace std;

/* Idea
Obviously, the largest element should be in front.
Therefore, the right cutoff should be right before the largest element.
The first parts are fixed to be the subarray from the largest element to 
the end, so the only relevant parts left is everything before the largest 
element.

For this part, it will first start with the flipped subarray, 
then the left subarray.
Suppose it's like
    (ab...z)(01...9) -> (9...10)(ab...z)
If anything in (9...10) is < a, then cutting off earlier to let a 
move forward is optimal.
Therefore need to flip the part up until right before it becomes < a.


FUCK MISSED A CORNER CASE
Largest element in front -> cannot have largest element in front in the result
In this case, we want to put the 2nd largest element in front instead, and the 
rest of the process stays the same.
This might cause issues when n=1 might as well hardcode that corner case out.


ANOTHER MISSED CORNER CASE
Largest element at the end -> another way to move to front is flip only it
In this case, use the alternative if a[0] > a[n-2] to make the ans[1] bigger.


CORNER CASE ELECTRIC BOOGALOO
Largest element in front and 2nd largest at end
-> flip only last element to get n-1 and n as first two elements
*/

int main() {
    // Loop for Homu test cases
    int Homu;
    cin >> Homu;
    for (int Kumi = 0; Kumi < Homu; Kumi++) {
        // Get the input
        int n;
        cin >> n;
        vector<int> p(n);
        for (int i = 0; i < n; i++) {
            int next;
            cin >> next;
            p.at(i) = next;
        }

        // VERY CORNER CASE
        if (n == 1) {
            cout << 1 << endl;
            continue;
        }

        // Get index of largest element (aka right exclusive cutoff)
        int R = 0;
        while (true) {
            if (p.at(R) != n) {
                R += 1;
            } else {
                break;
            }
        }
        // Corner case of largest in front
        if (R == 0) {
            while (true) {
                if (p.at(R) != n-1) {
                    R += 1;
                } else {
                    break;
                }
            }
        }

        // Get index of how far left we can go before dropping (aka left inclusive cutoff)
        int L = R-1;
        while (true) {
            if (L == 0) {   // If there is nothing to the left
                break;
            } else if (p.at(L-1) <= p.at(0)) {  // If including does not add a better element
                break;
            } else {   // If including adds a better element
                L -= 1;
            }
        }

        // Corner case of largest at the back and 1st > 2nd to last
        if (p.at(n-1) == n and p.at(0) > p.at(n-2)) {
            L = n-1;
            R = n;
        }
        // Corner case of largest in front and 2nd largest at the back
        if (p.at(0) == n and p.at(n-1) == n-1) {
            L = n-1;
            R = n;
        }

        // Construct the ans
        int l = L;
        int m = R-L;
        int r = n-R;

        // DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        // cout << "L = " << L << ", R = " << R << endl;
        // DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        vector<int> ans(n);
        for (int i = 0; i < r; i++) {
            ans.at(i) = p.at(l+m+i);
        }
        for (int i = 0; i < m; i++) {
            ans.at(r+i) = p.at(l+m-1-i);
        }
        for (int i = 0; i < l; i++) {
            ans.at(r+m+i) = p.at(i);
        }

        // Print the ans
        for (int i = 0; i < n; i++) {
            cout << ans.at(i) << ' ';
        }
        cout << endl;

    }

    return 0;
}
