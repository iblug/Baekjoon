import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();
        int c = readInt();

        System.out.println(a * b + c);
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