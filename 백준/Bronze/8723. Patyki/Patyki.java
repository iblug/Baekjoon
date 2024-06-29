import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();
        int c = readInt();
        int m = Math.max(a, Math.max(b, c));
        int n = Math.min(a, Math.min(b, c));

        if (a == b && b == c) {
            System.out.println(2);
        } else if (m*m == n*n + (a+b+c-m-n)*(a+b+c-m-n)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        return t;
    }
}