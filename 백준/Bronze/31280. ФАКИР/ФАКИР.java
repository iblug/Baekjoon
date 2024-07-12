import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] a = new int[4];
        for (int i = 0; i < 4; i++) {
            a[i] = readInt();
        }
        Arrays.sort(a);
        System.out.println(1 + a[1] + a[2] + a[3]);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}