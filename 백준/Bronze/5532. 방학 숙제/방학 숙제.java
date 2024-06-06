import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int l = readInt();
        int a = readInt();
        int b = readInt();
        int c = readInt();
        int d = readInt();

        System.out.println(l - Math.max((a+c-1)/c, (b+d-1)/d));
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