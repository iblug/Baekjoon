import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), k = readInt();
        System.out.println((n+k-m-1)/(k-m));
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}