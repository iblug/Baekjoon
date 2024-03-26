import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] c = br.readLine().toCharArray();
        dp = new int[26][c.length + 1];

        for (int i = 0; i < c.length; i++) {
            dp[c[i] - 'a'][i + 1] = 1;
        }
        for (int i = 0; i < 26; i++) {
            for (int j = 1; j <= c.length; j++) {
                dp[i][j] += dp[i][j - 1];
            }
        }

        int q = Integer.parseInt(br.readLine());

        StringTokenizer st;
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a;
        int l, r;
        while (q-- > 0) {
            st = new StringTokenizer(br.readLine());
            a = st.nextToken().charAt(0) - 'a';
            l = Integer.parseInt(st.nextToken());
            r = Integer.parseInt(st.nextToken());

            bw.write(String.valueOf(dp[a][r+1] - dp[a][l]));
            bw.write('\n');
        }

        bw.flush();
        bw.close();
    }
}