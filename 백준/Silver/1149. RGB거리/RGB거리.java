import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        int n = readInt();

        graph = new int[n][];
        for (int i = 0; i < n; i++) {
            graph[i] = new int[3];
            if (i == 0) {
                for (int j = 0; j < 3; j++) {
                    graph[i][j] = readInt();
                }
            } else {
                graph[i][0] = readInt() + Math.min(graph[i-1][1], graph[i-1][2]);
                graph[i][1] = readInt() + Math.min(graph[i-1][0], graph[i-1][2]);
                graph[i][2] = readInt() + Math.min(graph[i-1][0], graph[i-1][1]);
            }
        }
        System.out.println(Arrays.stream(graph[n-1]).min().getAsInt());
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