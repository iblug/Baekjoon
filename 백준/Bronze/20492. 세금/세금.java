import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        int n = readInt();
        StringBuilder sb = new StringBuilder();
        sb.append(n/1000 * 780).append(' ').append(n/1000 * (800 + 2 * 78));
        System.out.println(sb);
    }

    private int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + v - 48;
        }
        return t;
    }
}