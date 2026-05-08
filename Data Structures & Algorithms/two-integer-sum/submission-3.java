class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numbers = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            int number = nums[i];
            int rest = target - number;
            if(numbers.containsKey(rest)){
                return new int[] {numbers.get(rest), i};
            }
            numbers.put(number, i);
        }
        return new int[] {};
    }
}
