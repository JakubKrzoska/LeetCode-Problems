class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numbers = new HashSet<>();

        for(int num : nums){
            numbers.add(num);
        }

        int res = 0;
        for(int num : numbers){
            if(!numbers.contains(num-1)){
                int len = 1;
                while (numbers.contains(num + len)){
                    len++;
                }
                res = Math.max(res, len);
            }
        }
        return res;
    }
}
