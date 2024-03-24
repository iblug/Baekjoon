import java.io.IOException;

public class Main {
    static int n, m;
    static int[] lst;

    public static void main(String[] args) throws IOException {
        n = readInt();
        m = readInt();
        lst = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            lst[i] = lst[i - 1] + readInt();
        }

        StringBuilder sb = new StringBuilder();
        int s, e;
        for (int i = 0; i < m; i++) {
            s = readInt();
            e = readInt();
            sb.append(lst[e] - lst[s - 1]).append('\n');
        }

        System.out.println(sb);
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