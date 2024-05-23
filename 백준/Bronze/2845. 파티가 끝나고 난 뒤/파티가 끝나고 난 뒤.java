import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int l = readInt();
        int p = readInt();

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 5; i++) {
            sb.append(readInt() - l*p).append(" ");
        }

        System.out.println(sb);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }

        return t;
    }
}