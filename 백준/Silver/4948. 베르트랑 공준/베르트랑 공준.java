import java.io.IOException;

public class Main {
    static boolean[] prime;
    static final int NUM = 246913;

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        prime = new boolean[NUM];
        prime[0] = true;
        prime[1] = true;
        for (int i = 2; i < Math.sqrt(NUM) + 1; i++) {
            if (!prime[i]) {
                for (int j = 2 * i; j < NUM; j += i) {
                    prime[j] = true;
                }
            }
        }

        while (true) {
            int n = readInt();
            if (n == 0) break;
            int c = 0;
            for (int i = n + 1; i <= n * 2; i++) {
                if (!prime[i]) c++;
            }
            sb.append(c).append('\n');
        }
        System.out.println(sb);
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}