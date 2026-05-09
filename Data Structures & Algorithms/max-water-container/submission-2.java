class Solution {
    public int maxArea(int[] heights) {
        int res = 0;
        int l = 0, r = heights.length - 1;

        while(l < r){
            res = Math.max(res, (r - l) * Math.min(heights[r], heights[l]));
            if (heights[l] <= heights[r]) l++;
            else r--;
        }
        return res;
    }
}
