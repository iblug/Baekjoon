import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();

        System.out.println(((24-a) + b)%24);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 32) {
            t = 10 * t + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}