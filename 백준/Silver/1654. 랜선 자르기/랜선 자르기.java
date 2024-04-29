import java.io.IOException;

public class Main {
    static int[] data;

    public static void main(String[] args) throws IOException {
        int K = readInt();
        int N = readInt();
        
        data = new int[K];
        long max = 0;
        for (int i = 0; i < K; i++) {
            data[i] = readInt();
            max = Math.max(max, data[i]);
        }

        max++;
        long min = 0;
        long mid, sum;

        while (min < max) {
            mid = (max + min) / 2;
            sum = 0;

            for (int i = 0; i < K; i++) {
                sum += (data[i] / mid);
            }

            if (sum < N) {
                max = mid;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(min-1);
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 32) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}
