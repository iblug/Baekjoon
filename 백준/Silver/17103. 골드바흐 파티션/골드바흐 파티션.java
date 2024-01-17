import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        boolean[] prime = getPrime();
        int t = readInt();

        while (t-- > 0) {
            int n = readInt();
            int c = 0;
            for (int i = 2; i <= n/2; i++) {
                if (!prime[i] && !prime[n-i]) {
                    c++;
                }
            }
            sb.append(c).append('\n');
        }

        System.out.println(sb);
    }

    static boolean[] getPrime() {
        boolean[] prime = new boolean[1000001];
        prime[0] = true;
        prime[1] = true;
        for (int i = 2; i < Math.sqrt(1000001) + 1; i++) {
            if (!prime[i]) {
                for (int j = i * 2; j < 1000001; j += i) {
                    prime[j] = true;
                }
            }
        }
        return prime;
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}