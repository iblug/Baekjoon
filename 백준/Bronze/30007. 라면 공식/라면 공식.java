import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int N = readInt();
        int A, B, X;
        StringBuilder sb = new StringBuilder();

        while (N-- > 0) {
            A = readInt();
            B = readInt();
            X = readInt();

            sb.append(A*(X-1)+B).append('\n');
        }

        System.out.println(sb);
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 32) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}