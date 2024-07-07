import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        int a, b, n = readInt();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while (n-- > 0) {
            a = readInt();
            b = readInt();
            while (b-- > 0) {
                bw.write("X".repeat(a));
                bw.write('\n');
            }
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