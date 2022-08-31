#include <stdio.h>

int main() {
    // str stores the input string
    char str[101];
    fgets(str, 101, stdin);

    // exists[i] = 1 (True) if the ith letter exists, and 0 otherwise (0-indexed)
    int exists[26];
    for (int i = 0; i < 26; i++) {
        exists[i] = 0;   // Initialize all to "not exist"
    }

    // Linearly scan the string to check what letters appear
    int i = 0;
    while (str[i] != 0) {         // While not at the end of the string
        int ord = str[i] - 'a';   // Order of str[i] in the alphabet (0-indexed)
        exists[ord] = 1;        // Mark it as existing
        i += 1;                   // Go to next char
    }

    // Find the number of letters that exist
    int sum = 0;
    for (int i = 0; i < 26; i++) {
        sum += exists[i];
    }

    // Check parity and output accordingly
    if (sum%2 == 0) {
        puts("CHAT WITH HER!");
    } else {
        puts("IGNORE HIM!");
    }
}
