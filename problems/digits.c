#include <stdio.h>

void checkSameDigits(int N) {
    int digit = N % 10;
    while (N != 0) {
        int curr = N % 10;
        N /= 10;

        if(curr != digit) {
            printf("No");
            return;
        }
    }

    printf("Yes");
}

int main() {
    int N = 222;
    checkSameDigits(N);
    return 0;
}