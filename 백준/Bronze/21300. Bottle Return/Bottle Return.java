import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        System.out.println((readInt() + readInt() + readInt() + readInt() + readInt() + readInt()) * 5);
    }

    private int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + v - 48;
        }
        return t;
    }
}