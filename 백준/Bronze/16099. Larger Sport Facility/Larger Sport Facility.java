import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        long n = readLong();
        while (n-- > 0) {
            long t = readLong() * readLong();
            long e = readLong() * readLong();

            if (t > e) {
                System.out.println("TelecomParisTech");
            } else if (e > t) {
                System.out.println("Eurecom");
            } else {
                System.out.println("Tie");
            }
        }
    }

    private long readLong() throws IOException {
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