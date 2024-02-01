import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt(), k = readInt();
        int a = 1, b = 1, c = 1;
        for (int i = 1; i <= n; i++) {
            a *= i;
        }
        for (int i = 1; i <= k; i++) {
            b *= i;
        }
        for (int i = 1; i <= n - k; i++) {
            c *= i;
        }
        System.out.println(a / (b * c));
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}