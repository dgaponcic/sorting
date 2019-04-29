#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void *selection(int n, int arr[]) {
    int i, j, pos, max, temp;
    for(i = 0; i < n; i++) {
        max = arr[0];
        pos = 0;
        for(j = 1; j < n - i; j++) {
            if(max < arr[j]) {
                max = arr[j];
                pos = j;
            }
        }
        temp = arr[pos];
        arr[pos] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }
}

int main() {
    int i, n = 1000000;
    time_t t;
    int arr[n];

    srand((unsigned) time(&t));
    for(i = 0; i < n; i++)
        arr[i] = rand();
        // scanf("%d", &arr[i]);

    clock_t begin = clock();
    selection(n, arr);
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("execution time %f\n", time_spent);
    // for(i = 0; i < n; i++)
    //     printf("%d ", arr[i]);
    // printf("\n");
    return 0;
}