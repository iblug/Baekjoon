import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int k = readInt(), n = readInt(), m = readInt();
        System.out.println(Math.max(0, k*n - m));
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}