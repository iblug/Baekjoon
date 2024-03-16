import java.io.IOException;
import java.util.Arrays;

public class Main {
    static long[][] dp;

    public static void main(String[] args) throws IOException {
        int n = readInt();

        System.out.println(solution(n));
    }

    private static long solution(int n) {
        dp = new long[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new long[]{0, 1, 1, 1, 1, 1, 1, 1, 1, 1};
        }
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][0] = dp[i-1][1] % 1000000000;
                } else if (j == 9) {
                    dp[i][9] = dp[i-1][8] % 1000000000;
                } else {
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000;
                }
            }
        }
        return Arrays.stream(dp[n-1]).sum() % 1000000000;
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}