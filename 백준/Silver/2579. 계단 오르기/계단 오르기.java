import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[] graph;

    public static void main(String[] args) throws IOException {
        int n = readInt();

        graph = new int[n];
        for (int i = 0; i < n; i++) {
            graph[i] = readInt();
        }
        if (n < 3) {
            System.out.println(Arrays.stream(graph).sum());
        }
        else {
            int[] dp = new int[n];
            dp[0] = graph[0];
            dp[1] = graph[0] + graph[1];
            dp[2] = graph[2] + Math.max(graph[1], dp[0]);
            for (int i = 3; i < n; i++) {
                dp[i] = graph[i] + Math.max(dp[i-3]+graph[i-1], dp[i-2]);
            }
            System.out.println(dp[n-1]);
        }

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