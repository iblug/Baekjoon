import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> set = new HashMap<>();
        while (n-- > 0) {
            String s = br.readLine();
            if (s.length() >= m) {
                set.put(s, set.getOrDefault(s, 0) + 1);
            }

        }
        
        List<Map.Entry<String, Integer>> list = new ArrayList<>(set.entrySet());
        list.sort((e1, e2) -> e1.getKey().compareTo(e2.getKey()));
        list.sort((e1, e2) -> e2.getKey().length() - e1.getKey().length());
        list.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> entry : list) {
            sb.append(entry.getKey()).append("\n");
        }
        System.out.println(sb);
    }
}