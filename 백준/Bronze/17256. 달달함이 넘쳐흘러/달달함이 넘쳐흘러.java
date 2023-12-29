import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        int ax = readInt();
        int ay = readInt();
        int az = readInt();
        int cx = readInt();
        int cy = readInt();
        int cz = readInt();

        StringBuilder sb = new StringBuilder();
        sb.append(cx - az).append(' ').append(cy / ay).append(' ').append(cz - ax);
        System.out.println(sb);
    }

    private int readInt() throws IOException {
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