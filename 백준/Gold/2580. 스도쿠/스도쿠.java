import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
    static boolean[][] cr, cc, cs;
    static int[][] board;

    public static void main(String[] args) throws Exception {
        board = new int[9][9];
        cr = new boolean[9][];
        cc = new boolean[9][];
        cs = new boolean[9][];
        for (int i = 0; i < 9; i++) {
            cr[i] = new boolean[10];
            cc[i] = new boolean[10];
            cs[i] = new boolean[10];
        }
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int num = readInt();
                board[i][j] = num;

                if (num == 0) {
                    continue;
                }

                cr[i][num] = true;
                cc[j][num] = true;
                cs[(i / 3) * 3 + j / 3][num] = true;
            }
        }

        check(0);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                bw.write(String.valueOf(board[i][j]));
                bw.write(' ');
            }
            bw.write('\n');
        }

        bw.flush();
        bw.close();
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + v - 48;
        }
        if (t == 13) {
            System.in.read();
        }
        return t;
    }

    static boolean check(int d) {
        if (d == 81) {
            return true;
        }

        int row = d / 9;
        int col = d % 9;

        if (board[row][col] != 0) {
            return check(d + 1);
        }

        for (int n = 1; n <= 9; n++) {
            if (!cr[row][n] && !cc[col][n] && !cs[(row / 3) * 3 + col / 3][n]) {
                cr[row][n] = true;
                cc[col][n] = true;
                cs[(row / 3) * 3 + col / 3][n] = true;

                board[row][col] = n;
                if (check(d + 1)) {
                    return true;
                }

                board[row][col] = 0;
                cr[row][n] = false;
                cc[col][n] = false;
                cs[(row / 3) * 3 + col / 3][n] = false;
            }
        }

        return false;
    }
}