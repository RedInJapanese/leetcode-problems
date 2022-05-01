

int search(int* nums, int numsSize, int target){
    int left = numsSize/2;
    int right = numsSize;
    if(right>=1) {
        int mid = left+(right-1)/2;
        if(nums[mid] == target) {
            return mid;
        }
        if(nums[mid]>target) {
            return search(nums, right-1, target);
        }
        return search(nums, left+1, target);

    }
}

int main(void) {
    return 0;
}