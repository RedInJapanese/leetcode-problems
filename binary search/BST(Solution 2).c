
 #include <stdlib.h>
 #include <unistd.h>
 #include <stdio.h>

 struct TreeNode {
      int val;
      struct TreeNode *left;
      struct TreeNode *right;
 };
struct TreeNode* searchBST(struct TreeNode* root, int val){
    while(root) {
        if(root->val == val) {
            break;
        }
        if(root->val<val) {root = root->right;}
        else {root = root->left;}
    }
    return root;
}
int main(void) {
    return 0;
}
