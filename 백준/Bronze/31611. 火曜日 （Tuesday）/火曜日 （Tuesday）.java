import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int x = readInt();

        System.out.println(x % 7 == 2 ? 1 : 0 );
    }

    static int readInt() throws IOException {
        int v, t = 0;

        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }

        return t;
    }
}