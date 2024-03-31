import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int t = readInt();
        int m = readInt();

        if (t > 16 || m > 0 || t <= 11) {
            System.out.println(280);
        } else {
            System.out.println(320);
        }
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}