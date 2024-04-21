import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int t1, e1, f1, t2, e2, f2;
        t1 = readInt();
        e1 = readInt();
        f1 = readInt();
        t2 = readInt();
        e2 = readInt();
        f2 = readInt();

        int max = t1 * 3 + e1 * 20 + f1 * 120;
        int mel = t2 * 3 + e2 * 20 + f2 * 120;

        if (max > mel) {
            System.out.println("Max");
        } else if (max < mel) {
            System.out.println("Mel");
        } else {
            System.out.println("Draw");
        }
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