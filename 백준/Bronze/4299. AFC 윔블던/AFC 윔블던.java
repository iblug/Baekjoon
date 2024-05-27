import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();

        StringBuilder sb = new StringBuilder();
        if (a < b || (a + b) % 2 != 0) {
            sb.append(-1);
        } else {
            sb.append((a + b) / 2).append(" ").append((a - b) / 2);
        }

        System.out.println(sb);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }

        return t;
    }
}