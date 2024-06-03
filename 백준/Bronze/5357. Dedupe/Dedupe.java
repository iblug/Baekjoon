import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String s;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            char c;
            s = br.readLine();
            c = s.charAt(0);
            sb.append(c);
            for (int j = 1; j < s.length(); j++) {
                if (c != s.charAt(j)) {
                    sb.append(s.charAt(j));
                }
                c = s.charAt(j);
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}