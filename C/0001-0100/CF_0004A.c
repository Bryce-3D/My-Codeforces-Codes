#include <stdio.h>
 
int main() {
    int w;
    scanf("%d", &w);
    
    if (w%2 == 0 && w > 2) {
        puts("YES");
    } else {
        puts("NO");
    }
}
