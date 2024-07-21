import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] a = new int[3];
        for (int i = 0; i < 3; i++) {
            a[i] = readInt();
        }

        Arrays.sort(a);

        if (a[0] + a[1] == a[2]) {
            System.out.println(1);
        } else {
            System.out.println(0);
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