import java.util.HashMap;
import java.util.Map;

public class twoSum_solution {
    public int[] twoSum(int[] nums, int target) {
        //wow so cool iterate a billion times haha
        Map<Integer, Integer> map = new HashMap<>();
        int num;
        int diff;
        for (int i = 0; i < nums.length; i++) {
            num = nums[i];
            diff = target - num;

            if(map.containsKey(diff)){
                return new int[] {map.get(diff), i};
            }
        
            map.put(num, i);
        }
        return null;
    }

    public static void main(String[] args) {
        twoSum_solution twoSum = new twoSum_solution();
        int[] list = {1,2,3};
        System.out.println(twoSum.twoSum(list, 0));
    }
}
