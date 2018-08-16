import java.util.Arrays;
import java.util.HashMap;
public class TwoSum
{
    public int[] twoSum(int[] nums, int target)
    {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i=0; i<nums.length; i++)
        {
            int complement = target-nums[i];
            if(map.containsKey(complement))
            {
                return new int[] {map.get(complement), i};
            }
            else
            {
                map.put(nums[i], i);
            }
        }

        throw new IllegalArgumentException("No two sum solution.");
    }

    public static void main(String[] args)
    {
        TwoSum twosum = new TwoSum();
        int[] input = {2,3,4,6,3,6,4};
        int target = 8;
        int[] ans =  twosum.twoSum(input, target);
        System.out.println(Arrays.toString(ans));
    }
}