#include <stdio.h> 
#include <stdlib.h> 

int main(void) {
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int**returnColumnSizes){
    *returnSize = *matrixColSize;

    int **returnArr = (int**)calloc(*returnSize,sizeof(int*));
    *returnColumnSizes = (int*)calloc(*matrixColSize, sizeof(int));
    for(int i = 0; i<*matrixColSize; i++) {
        returnColumnSizes[i] = matrixSize;
        returnArr[i] = (int*)calloc(matrixSize, sizeof(int));     
    }   

    for(int x = 0; x<matrixSize; x++) {
        for(int y = 0; y< *matrixColSize; y++) {
            returnArr[x][y] = matrix[y][x];
        }
    }
    return returnArr;
}