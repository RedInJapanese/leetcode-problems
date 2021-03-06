#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


int **generateMatrix(int n, int* returnSize, int** returnColumnSizes);

int **generateMatrix(int n, int* returnSize, int** returnColumnSizes){
    returnSize = (int*)malloc((n*n)*sizeof(int));
    returnColumnSizes = (int**)calloc(n,sizeof(int*));
    for(int l = 0; l<n; l++) {
	    returnColumnSizes[l] = (int*)calloc(n, sizeof(int));
    }
    int x = 1;
    int y = 0;
    for(int i = 0;i <(n*n); i++) {
        returnSize[i] = x;
        x++;
    }
    for(int j = 0; j<n; j++) {
        returnColumnSizes[0][j] = returnSize[y];
        y++;
    }
    for(int k = 0; k<n; k++) {
        returnColumnSizes[k][n-1]= returnSize[y];
        y++;
    }
    return returnColumnSizes;

}

int main(void) {
    int n = 3; 
    int* returnS = NULL;
    int **returnC = NULL;
    returnC = generateMatrix(n, returnS, returnC);

    for(int o = 0; o<n; o++) {
        for(int m = 0; m<n; m++) {
            printf("%d\n", returnC[o][m]);
        }
    }
    return 0;
}

