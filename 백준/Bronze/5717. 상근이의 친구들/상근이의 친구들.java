import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int s;
        while (true) {
            s = readInt() + readInt();
            if (s == 0) {
                break;
            }
            sb.append(s).append('\n');
        }

        System.out.println(sb);
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