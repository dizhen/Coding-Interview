class Solution {
    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return false;
        int left = 0;
        int right = nums.length-1;
        while (left < right) {
            int mid = (right-left)/2 + left;
            if (nums[mid] == target) return true;
            if (nums[left] == nums[mid] && nums[right] == nums[mid]) {
                left++;
                right--;
            } else if (nums[mid] <= nums[right]) {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid+1;
                } else {
                    right = mid;
                }
            } else {
                if (nums[left] <= target && target <= nums[mid]) {
                    right = mid;
                } else {
                    left = mid+1;
                }
            }
        }
        if (nums[left] == target) return true;
        else return false;
    }
}
