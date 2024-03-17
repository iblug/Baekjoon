import java.io.IOException;

public class Main {
    static int[] data;
    static int n;

    public static void main(String[] args) throws IOException {
        n = readInt();
        data = new int[n];
        for (int i = 0; i < n; i++) {
            data[i] = readInt();
        }
        
        System.out.println(solution());
    }

    private static int solution() {
        int[] dp = new int[n];
        dp[0] = data[0];
        if (n > 1) {
            dp[1] = data[0] + data[1];
        }
        if (n > 2) {
            dp[2] = Math.max(Math.max(data[2] + data[1], data[2] + data[0]), dp[1]);
            for (int i = 3; i < n; i++) {
                dp[i] = Math.max(Math.max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i]), dp[i - 1]);
            }
        }

        return dp[n-1];
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