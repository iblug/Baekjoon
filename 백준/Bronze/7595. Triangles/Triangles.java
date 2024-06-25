import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = 0;
        while ((n = readInt()) != 0) {
            for (int i = 1; i <= n; i++) {
                bw.write("*".repeat(i));
                bw.write('\n');
            }
        }

        bw.flush();
        bw.close();
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