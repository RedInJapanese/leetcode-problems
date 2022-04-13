#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


void generateMatrix(int n, int* returnSize, int** returnColumnSizes);

void generateMatrix(int n, int* returnSize, int** returnColumnSizes){
    returnSize = (int*)malloc((n*n)*sizeof(int));
    returnColumnSizes = (int**)malloc(n*sizeof(int*));
    for(int i = 0;i <(n*n); i++) {
        returnSize[i] = i;
        printf("%d\n", returnSize[i]);
    }

}

int main(void) {
    int n = 3; 
    int* returnS;
    int **returnC;
    generateMatrix(n, returnS, returnC);
    return 0;
}