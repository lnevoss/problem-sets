import java.util.HashMap;
import java.util.Map;

public class isAnagram_solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> charMapS = new HashMap<>();
        Map<Character, Integer> charMapT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if(charMapS.containsKey(s.charAt(i))){
                charMapS.put(s.charAt(i), charMapS.get(s.charAt(i))+1);
            } else{
                charMapS.put(s.charAt(i), 1);
            }
        }

        for (int j = 0; j < t.length(); j++) {
            if(charMapT.containsKey(t.charAt(j))){
                charMapT.put(t.charAt(j), charMapT.get(t.charAt(j))+1);
            } else{
                charMapT.put(t.charAt(j), 1);
            }
        }
        return charMapS.equals(charMapT);
    }

    public static void main(String[] args) {
        isAnagram_solution isAnagram = new isAnagram_solution();
        String s = "racecar";
        String t = "carrace";
        System.out.println(isAnagram.isAnagram(s, t));
    }
}
