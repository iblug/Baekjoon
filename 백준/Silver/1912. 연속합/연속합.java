import java.io.IOException;

public class Main {
    static int[] dp, arr;
    public static void main(String[] args) throws IOException {
        int n = readInt();

        arr = new int[n];
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = readInt();
        }
        dp[0] = arr[0];

        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(dp[i-1] + arr[i], arr[i]);
        }

        int ans = -Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, dp[i]);
        }

        System.out.println(ans);
    }

    private static int readInt() throws IOException {
        int t = 0;
        byte v;
        while ((v = read()) <= 32);
        boolean negative = (v == '-');
        if (negative) v = read();
        do {
            t = t * 10 + (v - '0');
        } while ((v = read()) >= '0' && v <= '9');
        return (negative) ? -t : t;
    }

    static final int SIZE = 1 << 13;
    static byte[] buffer = new byte[SIZE];
    static int index, size;
    private static byte read() throws IOException {
        if (index == size) {
            size = System.in.read(buffer, index = 0, SIZE);
            if (size < 0) buffer[0] = -1;
        }
        return buffer[index++];
    }
}