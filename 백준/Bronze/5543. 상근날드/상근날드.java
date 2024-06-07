import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();
        int c = readInt();
        int d = readInt();
        int e = readInt();

        System.out.println(Math.min(a, Math.min(b, c)) + Math.min(d, e) - 50);

    }

    private static int readInt() throws IOException {
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