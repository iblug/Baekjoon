import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int k = readInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = readInt();
        }

        int r = 0;
        while (n-- > 0) {
            r += k / arr[n];
            k %= arr[n];
        }

        System.out.println(r);
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