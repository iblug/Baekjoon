import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        int n = readInt();

        dp = new int[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[i+3];
            dp[i][0] = -1;
            dp[i][i+2] = -1;
            if (i == 0) {
                for (int j = 1; j < i+2; j++) {
                    dp[i][j] = readInt();
                }
            } else {
                for (int j = 1; j < i + 2; j++) {
                    dp[i][j] = readInt() + Math.max(dp[i-1][j-1], dp[i-1][j]);
                }
            }
        }
        System.out.println(Arrays.stream(dp[n-1]).max().getAsInt());
    }

    private static int readInt() throws IOException {
        int value = 0;
        byte v;
        while ((v = read()) <= ' ') ;
        do {
            value = value * 10 + v - '0';
        } while ((v = read()) >= '0' && v <= '9');
        return value;
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