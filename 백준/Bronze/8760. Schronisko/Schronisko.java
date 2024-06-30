import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();

        StringBuilder sb = new StringBuilder();
        int w, k;
        while (n-- > 0) {
            w = readInt();
            k = readInt();
            sb.append((w*k)/2).append('\n');
        }
        System.out.println(sb);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        return t;
    }
}