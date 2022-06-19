#include <stdio.h>
#include <unistd.h>
#include <stdlib.h> 
#include <math.h>

void rotate(int* nums, int numsSize, int k);

int main(void) {
    puts("lol"); 
    return 0;
}

void rotate(int* nums, int numsSize, int k){
    int *rotate = (int*)calloc(numsSize, sizeof(int));
    
    for(int i = 0; i<numsSize; ++i) {
        int move = abs((i+numsSize-(k%numsSize))%numsSize);
        rotate[i] = nums[move];
    }
    for(int x = 0; x<numsSize; ++x) {
        nums[x] = rotate[x];
    }
}