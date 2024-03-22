import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a, b, c;
        a = readInt();
        b = readInt();
        c = readInt();
        System.out.println(b/a*c*3);
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