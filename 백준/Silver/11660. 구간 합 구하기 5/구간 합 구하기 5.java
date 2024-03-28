import java.io.IOException;

public class Main {
    static int[][] dp;
    static int n, m;

    public static void main(String[] args) throws IOException {
        n = readInt();
        m = readInt();

        dp = new int[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1] + readInt() - dp[i-1][j-1];
            }
        }

        StringBuilder sb = new StringBuilder();
        int x1, y1, x2, y2;
        while (m-- > 0) {
            x1 = readInt();
            y1 = readInt();
            x2 = readInt();
            y2 = readInt();

            sb.append(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]).append('\n');
        }
        System.out.println(sb);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}