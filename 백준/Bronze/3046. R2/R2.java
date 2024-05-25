import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int r1 = readInt();
        int s = readInt();

        System.out.println(2 * s - r1);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }

        return t;
    }
}