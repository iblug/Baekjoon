import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] ans;
    static boolean[] v;
    static int n, m;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        ans = new int[m];
        v = new boolean[n];

        b(n, m, 0);

        System.out.println(sb);
    }

    static void b(int x, int y, int t) {
        if (t == m) {
            for (int e : ans) {
                sb.append(e).append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!v[i]) {
                v[i] = true;
                ans[t] = i + 1;
                b(n, m, t + 1);

                v[i] = false;
            }
        }
    }
}