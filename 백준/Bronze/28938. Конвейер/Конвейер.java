import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int N = readInt();
        int sum = 0;

        while (N-- > 0) {
            sum += readInt();
        }
        System.out.println(sum < 0 ? "Left" : sum > 0 ? "Right" : "Stay");
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        boolean f = false;
        while ((v = System.in.read()) > 32) {
            if (v == '-') {
                f = true;
                continue;
            }
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return f ? -t : t;
    }
}