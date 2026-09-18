import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class groupAnagrams_solution {
    
    /*
        We're creating an array filled with 0.
        The array is 26 characters long, so 26 unique letters that we can have.
        Then we itterate over each character and compare it to 'a'. 
        Here we're comparing ASCII values of those characters, finding
        the difference between them, that difference beeing the index
        of the character we currently have, and incrementing that value by one,
        marking the number of such characters in a word. In the end we put it all 
        into a map and group them by their newly mapped values.
        */
    
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> ans = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            

            String key = Arrays.toString(count);
            if (!ans.containsKey(key)) {
                ans.put(key, new ArrayList<>());
            }

            ans.get(key).add(s);
        }

        return new ArrayList<>(ans.values());
    }
}
