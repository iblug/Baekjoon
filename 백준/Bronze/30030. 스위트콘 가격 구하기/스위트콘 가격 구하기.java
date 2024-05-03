import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int B = readInt();

        System.out.println(B*10/11);
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 32) {
            t = t * 10 + (v - 48);
        }

        return t;
    }
}