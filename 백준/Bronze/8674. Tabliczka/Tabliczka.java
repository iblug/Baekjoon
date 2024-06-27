import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        long a = readInt();
        long b = readInt();
        if (a % 2 == 1 && b % 2 == 1) {
            System.out.println(Math.min(a, b));
        } else {
            System.out.println(0);
        }

    }

    static long readInt() throws IOException {
        int v;
        long t = 0L;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        return t;
    }
}