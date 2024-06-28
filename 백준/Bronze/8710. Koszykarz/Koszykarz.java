import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();
        int c = readInt();
        System.out.println((b - a + c - 1) / c);

    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        return t;
    }
}