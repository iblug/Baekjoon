import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int N = readInt();
        int even = 0;
        int odd = 0;

        while (N-- > 0) {
            if (readInt() % 2 == 1) {
                odd++;
            } else {
                even++;
            }
        }

        System.out.println(even > odd ? "Happy" : "Sad");
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 32) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}
