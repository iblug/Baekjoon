import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int b = readInt();
        int c = readInt();
        int d = readInt();
        if (a > b && b > c && c > d) {
            System.out.println("Fish Diving");
        } else if (a < b && b < c && c < d) {
            System.out.println("Fish Rising");
        } else if (a == b && b == c && c == d) {
            System.out.println("Fish At Constant Depth");
        } else {
            System.out.println("No Fish");
        }
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}