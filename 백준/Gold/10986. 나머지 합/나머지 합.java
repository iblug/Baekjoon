import java.io.IOException;

public class Main {
    static int[] cnt;
    static int n, m;

    public static void main(String[] args) throws IOException {
        n = readInt();
        m = readInt();
        cnt = new int[m];

        int s = 0;
        for (int i = 0; i < n; i++) {
            s = (s + readInt()) % m;
            cnt[s%m]++;
        }

        System.out.println(solution());
    }

    private static long solution() {
        long r = cnt[0];
        for (int i = 0; i < m; i++) {
            r += (long) cnt[i] * (cnt[i] - 1) / 2;
        }
        return r;
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}