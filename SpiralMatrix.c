#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


void generateMatrix(int n, int* returnSize, int** returnColumnSizes);

void generateMatrix(int n, int* returnSize, int** returnColumnSizes){
    returnSize = (int*)malloc((n*n)*sizeof(int));
    returnColumnSizes = (int**)malloc(n*sizeof(int*));
    int x = 1;
    for(int i = 0;i <(n*n); i++) {
        returnSize[i] = x;
        printf("%d ", returnSize[i]);
	x++;
    }
    printf("\n");

}

int main(void) {
    int n = 3; 
    int* returnS = NULL;
    int **returnC = NULL;
    generateMatrix(n, returnS, returnC);
    return 0;
}

