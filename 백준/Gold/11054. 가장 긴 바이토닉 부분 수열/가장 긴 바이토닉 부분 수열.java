import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[] data, dp_l, dp_r, dp;
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
        bi_l();
        bi_r();
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = dp_l[i] + dp_r[i];
        }

        return Arrays.stream(dp).max().getAsInt() - 1;

    }

    private static void bi_l() {
        dp_l = new int[n];
        for (int i = 0; i < n; i++) {
            dp_l[i] = 1;
            for (int j = 0; j < i; j++) {
                if (data[j] < data[i]) {
                    dp_l[i] = Math.max(dp_l[i], dp_l[j] + 1);
                }
            }
        }
    }

    private static void bi_r() {
        dp_r = new int[n];
        for (int i = n - 1; i > -1; i--) {
            dp_r[i] = 1;
            for (int j = n - 1; j > i; j--) {
                if (data[j] < data[i]) {
                    dp_r[i] = Math.max(dp_r[i], dp_r[j] + 1);
                }
            }
        }
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