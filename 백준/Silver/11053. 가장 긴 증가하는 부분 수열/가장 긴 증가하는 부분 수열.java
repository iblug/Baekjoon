import java.io.IOException;
import java.util.Arrays;

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
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (data[j] < data[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        return Arrays.stream(dp).max().getAsInt();
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