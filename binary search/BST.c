
 #include <stdlib.h>
 #include <unistd.h>
 #include <stdio.h>

 struct TreeNode {
      int val;
      struct TreeNode *left;
      struct TreeNode *right;
 };
struct TreeNode* searchBST(struct TreeNode* root, int val){
    if(!root || root->val == val) {
        return root;
    }
    if(root->val<val) {
        return searchBST(root->right, val);
    }
    return searchBST(root->left, val);
}
int main(void) {
    return 0;
}