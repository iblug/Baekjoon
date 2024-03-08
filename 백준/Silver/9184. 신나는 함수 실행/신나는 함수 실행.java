import java.io.IOException;

public class Main {
    static int[][][] dp;
    public static void main(String[] args) throws IOException {
        int a, b, c;
        dp = new int[21][21][21];
        StringBuilder sb = new StringBuilder();
        while (true) {
            a = readInt();
            b = readInt();
            c = readInt();
            if (a == -1 && b == -1 && c == -1) {
                break;
            }
            sb.append("w(").append(a).append(", ").append(b).append(", ").append(c).append(") = ").append(w(a, b, c)).append("\n");
//            System.out.printf("w(%d, %d, %d) = %d\n", a, b, c, w(a, b, c));
        }
        System.out.println(sb);

    }

    static int readInt() throws IOException {
        int v, t = 0;
        boolean f = false;
        while ((v = System.in.read()) > 32) {
            if (v == '-') {
                f = true;
                continue;
            }
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return f ? -t : t;
    }

    static int w(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0) {
            return 1;
        }
        else if (a > 20 || b > 20 || c > 20) {
            return w(20, 20, 20);
        }
        else if (dp[a][b][c] != 0) {
            return dp[a][b][c];
        }
        else if (a < b && b < c) {
            return dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
        }
        else {
            return dp[a][b][c] = w(a - 1, b, c) + w(a -1, b - 1, c) + w(a - 1, b, c -1) - w(a - 1, b - 1, c - 1);
        }
    }
}