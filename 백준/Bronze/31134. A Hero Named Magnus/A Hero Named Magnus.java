import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int n, t = readInt();
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            n = readInt();
            sb.append((long)2*n-1);
            sb.append('\n');
        }
        System.out.println(sb);
    }

    static int readInt() throws IOException {
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