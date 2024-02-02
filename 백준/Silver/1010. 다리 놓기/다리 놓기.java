import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int t = readInt();
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = readInt(), m = readInt();
            long a = 1;
            for(int i = 0; i < n; i++) {
                a *= (m - i);
                a /= (i + 1);
            }
            sb.append(a).append("\n");
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