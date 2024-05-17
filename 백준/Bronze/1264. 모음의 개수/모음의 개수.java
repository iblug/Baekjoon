import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String s;
        int cnt;
        while (true) {
            cnt = 0;
            s = br.readLine().toLowerCase();
            if (s.equals("#")) {
                break;
            }
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u') {
                    cnt++;
                }
            }
            sb.append(cnt).append('\n');
        }

        System.out.println(sb);
    }
}