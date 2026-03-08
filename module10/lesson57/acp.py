# Recurrence Relations
# Outline:
# Print the recurrence relation of the following recursive functions given.
# include <studio.h>
# Recursive function
#include <stdio.h>

#  Recursive function
int f(int n) {
    if (n <= 1)
        return 1;
    else
        return f(n - 1) + f(n - 1);
}

int main() {
    int n;

    printf("Enter value of n: ");
    scanf("%d", &n);

    int result = f(n);

    printf("Result: %d\n", result);

    printf("\nRecurrence Relation:\n");
    printf("T(n) = 2T(n-1) + O(1)\n");

    printf("\nTime Complexity:\n");
    printf("O(2^n)\n");

    printf("\nSpace Complexity:\n");
    printf("O(n)\n");

    return 0;
}