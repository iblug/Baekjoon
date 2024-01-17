import java.io.IOException;

public class Main {
    static boolean[] prime;
    static int NUM = 1000001;

    public static void main(String[] args) throws IOException {
        prime = new boolean[NUM];
        prime[0] = true;
        prime[1] = true;
        int t = readInt();

        getPrime();

        while (t-- > 0) {
            int n = readInt();
            int c = 0;
            for (int i = 2; i <= n/2; i++) {
                if (!prime[i] && !prime[n-i]) {
                    c++;
                }
            }
            System.out.println(c);
        }
    }

    static void getPrime() {
        for (int i = 2; i < Math.sqrt(NUM) + 1; i++) {
            if (!prime[i]) {
                for (int j = i * 2; j < NUM; j += i) {
                    prime[j] = true;
                }
            }
        }
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}