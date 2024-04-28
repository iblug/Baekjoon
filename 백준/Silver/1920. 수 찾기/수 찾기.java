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

//        System.out.println(Arrays.toString(arr));

        int M = readInt();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            int t = readInt();
//            System.out.println(t);
            sb.append(biSear(t, 0, N - 1)).append('\n');
        }

        System.out.println(sb);
    }

    private static int biSear(int target, int start, int end) {
        if (start > end) {
            return 0;
        }
        int mid = (start + end) / 2;

        if (arr[mid] == target) {
            return 1;
        } else if (arr[mid] > target) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }

        return biSear(target, start, end);
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