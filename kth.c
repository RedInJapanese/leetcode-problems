#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

 struct TreeNode {
      int val;
      struct TreeNode *left;
      struct TreeNode *right;
 };


int kthSmallest(struct TreeNode* root, int k){
    int size = 0;
    struct TreeNode* base = root;
    while(root) {
        root = root->left;
        size++;
    }
    int left_side[size+1];
    int i = size;
    root= base; 
    while(root) {
        left_side[i] = root->val;
        root = root->left;
        i--;
    }
    return left_side[k];
}

int main(void) {
    puts("test"); 
    return 0;
}