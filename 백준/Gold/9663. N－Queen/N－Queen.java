import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n, cnt;
    static boolean[] col, lt, rt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        col = new boolean[n];
        lt = new boolean[3 * n - 1];
        rt = new boolean[3 * n - 1];

        nQueen(0);

        System.out.println(cnt);
    }

    static void nQueen(int r) {
        if (r == n) {
            cnt++;
            return;
        }
        for (int c = 0; c < n; c++) {
            if (col[c] || lt[n + c - r] || rt[c + r]) {
                continue;
            }
            col[c] = true;
            lt[n + c - r] = true;
            rt[c + r] = true;

            nQueen(r + 1);

            col[c] = false;
            lt[n + c - r] = false;
            rt[c + r] = false;
        }
    }
}