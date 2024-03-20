import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[][] data;
    static int[] dp;
    static int n;

    public static void main(String[] args) throws IOException {
        n = readInt();

        data = new int[n][];
        for (int i = 0; i < n; i++) {
            data[i] = new int[2];
            data[i][0] = readInt();
            data[i][1] = readInt();
        }
        Arrays.sort(data, (o1, o2) -> o1[0] - o2[0]);

        System.out.println(solution());
    }

    private static int solution() {
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (data[i][1] > data[j][1]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        return n - Arrays.stream(dp).max().getAsInt();
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