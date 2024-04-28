import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[] arr;

    public static void main(String[] args) throws IOException {
        int N = readInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = readInt();
        }

        Arrays.sort(arr);

        int M = readInt();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            sb.append(Arrays.binarySearch(arr, readInt()) >= 0 ? 1 : 0).append('\n');
        }

        System.out.println(sb);
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        boolean f = false;
        while ((v = System.in.read()) > 32) {
            if (v == '-') {
                f = true;
                continue;
            }
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return f ? -t : t;
    }
}