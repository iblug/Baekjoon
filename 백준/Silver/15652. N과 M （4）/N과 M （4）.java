import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[] ans;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        ans = new int[m];
        c(1, 0);

        bw.flush();
        bw.close();
    }

    static void c(int a, int t) throws IOException {
        if (t == m) {
            for (int i : ans) {
                bw.write(String.valueOf(i));
                bw.write(' ');
            }
            bw.write('\n');
            return;
        }
        for (int i = a; i <= n; i++) {
            ans[t] = i;
            c(i, t + 1);
        }
    }
}
