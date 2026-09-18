import java.util.HashSet;
import java.util.Set;

class hasDuplicates_solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            if(set.contains(i)) return true;
            set.add(i);
        }
        return false;
    }

    public static void main(String[] args) {
        hasDuplicates_solution hasDuplicates = new hasDuplicates_solution();
        int[] list = {1,2,3};
        System.out.println(hasDuplicates.hasDuplicate(list));
    }
}
