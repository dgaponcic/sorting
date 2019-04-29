#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int *bubble1(int n, int *arr) {
    int i, j, temp;
    for(i = 0; i < n - 1; i++)
        for(j = 0; j < n - i - 1; j++)
            if(arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
    return arr;
}

int *bubble2(int n, int *arr) {
    int i, j, temp, flag = 1;
    while(flag == 1)
        for(i = 0; i < n - 1; i++) {
            flag = 0;
            for(j = 0; j < n - 1; j++)
                if(arr[j] > arr[j + 1]) {
                    flag = 1;
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
        }
    return arr;
}

int *bubble(int n, int *arr) {
    int i, j, temp;
    for(i = 0; i < n - 1; i++)
        for(j = 0; j < n - 1; j++)
            if(arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
    return arr;
}

int main() {
    int i, n = 5;
    int *arr = malloc(sizeof(int) * n);
    for(i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    arr = bubble2(n, arr);
    for(i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}