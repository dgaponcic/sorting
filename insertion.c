#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int *insertion(int n, int *arr) {
    int i, value, place;
    for(i = 1; i < n; i++) {
        value = arr[i];
        place = i;
        while(place > 0 && arr[place - 1] > value) {
            arr[place] = arr[place - 1];
            place--;
        }
        arr[place] = value;
    }
    return arr;
}

int findLocation(int *arr, int value, int low, int high) {
    int middle = (low + high) / 2;
    if(high <= low && value > arr[low]) return low + 1;
    if(high <= low && value <= arr[low]) return low;
    if(value == arr[middle]) return middle + 1;
    if(value < arr[middle]) return findLocation(arr, value, low, middle - 1);
    return findLocation(arr, value, middle + 1, high);
}

int *binaryInsertion(int n, int *arr) {
    int i, value, place, location;
    for(i = 1; i < n; i++) {
        value = arr[i];
        place = i;
        location = findLocation(arr, value, 0, place - 1);
        while(place > location) {
            arr[place] = arr[place - 1];
            place--;
        }
        arr[place] = value;
    }
    return arr;
}

int main() {
    int i, n = 5;
    int *arr = malloc(sizeof(int) * n);
    for(i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    arr = binaryInsertion(n, arr);
    for(i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}