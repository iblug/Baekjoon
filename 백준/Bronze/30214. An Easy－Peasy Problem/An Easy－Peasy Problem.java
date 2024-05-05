import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();

        System.out.println(2 * a < b ? "H" : "E");
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 32) {
            t = 10 * t + (v - 48);
        }
        return t;
    }
}