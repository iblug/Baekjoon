import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int r;
        int n = readInt();
        for (int i = 1; i <= n; i++) {
            r = readInt();
            r += readInt();
            bw.write("Case ");
            bw.write(String.valueOf(i));
            bw.write(": ");
            bw.write(String.valueOf(r));
            bw.write('\n');
        }

        bw.flush();
        bw.close();
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}