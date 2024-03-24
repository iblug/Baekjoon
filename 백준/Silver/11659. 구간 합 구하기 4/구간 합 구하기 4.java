import java.io.IOException;

public class Main {
    static int n, m;
    static int[] lst;

    public static void main(String[] args) throws IOException {
        n = readInt();
        m = readInt();
        lst = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            lst[i] = lst[i - 1] + readInt();
        }

        StringBuilder sb = new StringBuilder();
        int s, e;
        for (int i = 0; i < m; i++) {
            s = readInt();
            e = readInt();
            sb.append(lst[e] - lst[s - 1]).append('\n');
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