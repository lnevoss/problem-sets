import java.util.ArrayList;
import java.util.List;

public class stringEncodeDecode_solution {
    public static void main(String[] args) {
        stringEncodeDecode_solution solution = new stringEncodeDecode_solution();
        String encoded = solution.encode(new ArrayList<>());
        List<String> decoded = solution.decode(encoded);
        System.out.println(encoded);
        System.out.println(decoded);
    }

    public String encode(List<String> strs) {
        StringBuilder encodedString = new StringBuilder();
        for (String str : strs) {
            encodedString.append(str.length()).append(" ").append(str);
        }
        return encodedString.toString();
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != ' ') j++;

            int length = Integer.valueOf(str.substring(i, j));
            i = j + 1 + length;
            list.add(str.substring(j + 1, i));
        }
        return list;
    }
}
