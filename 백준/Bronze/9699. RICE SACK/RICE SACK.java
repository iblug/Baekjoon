import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int t, m;
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 1; i <= n; i++) {
            m = 0;
            for (int j = 0; j < 5; j++) {
                t = readInt();
                if (m < t) {
                    m = t;
                }
            }
            bw.write("Case #");
            bw.write(String.valueOf(i));
            bw.write(": ");
            bw.write(String.valueOf(m));
            bw.write('\n');
        }

        bw.flush();
        bw.close();
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        return t;
    }
}