import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashSet<String> set = new HashSet<>();
        int cnt = 0;
        while (n-- > 0) {
            String s = br.readLine();
            if (s.equals("ENTER")) {
                cnt += set.size();
                set = new HashSet<>();
            } else {
                set.add(s);
            }
        }
        cnt += set.size();
        System.out.println(cnt);
    }
}