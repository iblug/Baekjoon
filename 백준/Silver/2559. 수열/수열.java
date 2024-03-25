import java.io.IOException;

public class Main {
    static int n, k, ans;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        n = readInt();
        k = readInt();
        ans = Integer.MIN_VALUE;
        arr = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            arr[i] = arr[i - 1] + readInt();
        }

        for (int i = 1; i + k - 1 <= n; i++) {
            ans = Math.max(ans, arr[i + k - 1] - arr[i - 1]);
        }

        System.out.println(ans);
    }

    private static int readInt() throws IOException {
        int t = 0;
        byte v;
        while ((v = read()) <= 32) ;
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