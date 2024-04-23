import java.io.IOException;

public class Main {
    static int[][] board;
    static int white, blue;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = readInt();
            }
        }

        f(0, 0, n);

        System.out.println(white);
        System.out.println(blue);
    }

    static void f(int r, int c, int s) {
        if (check(r, c, s)) {
            if (board[r][c] == 0) {
                white++;
            } else {
                blue++;
            }
            return;
        }

        s = s / 2;

        f(r, c, s);
        f(r + s, c, s);
        f(r, c + s, s);
        f(r + s, c + s, s);
    }

    static boolean check(int r, int c, int s) {
        int color = board[r][c];

        for (int i = r; i < r + s; i++) {
            for (int j = c; j < c + s; j++) {
                if (board[i][j] != color) {
                    return false;
                }
            }
        }

        return true;
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }

        return t;
    }
}