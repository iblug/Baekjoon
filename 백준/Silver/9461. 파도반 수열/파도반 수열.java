import java.io.IOException;

public class Main {
    static long[] dp;

    public static void main(String[] args) throws IOException {
        dp = new long[100];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 1;
        int t = readInt();

        while (t-- > 0) {
            int n = readInt();
            System.out.println(f(n - 1));
        }
    }

    static long f(int n) {
        if (dp[n] != 0) {
            return dp[n];
        }
        return dp[n] = f(n - 3) + f(n - 2);
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