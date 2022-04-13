#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


void generateMatrix(int n, int* returnSize, int** returnColumnSizes);

void generateMatrix(int n, int* returnSize, int** returnColumnSizes){
    returnSize = (int*)malloc((n*n)*sizeof(int));
    returnColumnSizes = (int**)malloc((n*n)*sizeof(int*));
    int x = 1;
    int y = 0;
    for(int i = 0;i <(n*n); i++) {
        returnSize[i] = x;
        x++;
    }
    for(int j = 0; j<n; j++) {
        for(int k = 0; k<n; k++) {
            returnColumnSizes[j][k] = returnSize[y];
            printf("%d ", returnColumnSizes[j][k]);
            y++;
        }
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

