import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String s, n;
        int a, w;
        StringTokenizer st;
        while (true) {
            s = br.readLine();
            if (s.equals("# 0 0")) {
                break;
            }
            st = new StringTokenizer(s);
            n = st.nextToken();
            a = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            if (a > 17 || w >= 80) {
                sb.append(n).append(" Senior\n");
            } else {
                sb.append(n).append(" Junior\n");
            }
        }

        System.out.println(sb);
    }
}