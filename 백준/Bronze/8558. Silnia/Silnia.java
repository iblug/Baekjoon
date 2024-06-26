import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int r = 1;
        for (int i = 1; i <= n; i++) {
            r = r * i % 10;
        }
        System.out.println(r);

    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        return t;
    }
}