import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class topKFrequent_solution {

    /*
        My first idea was to create a map with keys as numbers 
        and values as their frequency, after which we would
        reverse sort by values and pick the k top values.
        In reality Java doesn't give any built in tools for this,
        so this solution lies elsewhere, not here.

        In the current solution we create a map that stores not
        number to frequency but a frequency to number, meaning that
        all numbers that we encounter i times are going to be stored
        under same key in an array. At the all we have to do is go
        through that array in reverse order k times and pick the 
        first values that we need.
    */
    
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        @SuppressWarnings("unchecked")
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int n : freq[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        topKFrequent_solution topFrequent = new topKFrequent_solution();
        int[] list = {1, 1, 2,2,2,2,3,3,3};
        System.out.println(Arrays.toString(topFrequent.topKFrequent(list, 2)));
    }
}