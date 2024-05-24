import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = 0;
        int s;

        for (int i = 0; i < 5; i++) {
            s = readInt();
            if (s < 40) {
                s = 40;
            }
            a += s;
        }

        System.out.println(a/5);
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