import java.io.IOException;

public class Main {
    static int n, k;
    static int[][] items, dp;

    public static void main(String[] args) throws IOException {
        n = readInt();
        k = readInt();
        dp = new int[k+1][n+1];

        items = new int[n+1][2];
        for (int i = 1; i <= n; i++) {
            items[i][0] = readInt();
            items[i][1] = readInt();
        }

        System.out.println(knapsack());
    }

    private static int knapsack() {
        int w;
        int v;
        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n; j++) {
                w = items[j][0];
                v = items[j][1];
                if (w <= i) {
                    dp[i][j] = Math.max(dp[i][j-1], dp[i-w][j-1] + v);
                } else {
                    dp[i][j] = dp[i][j-1];
                }
            }
        }
        return dp[k][n];
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