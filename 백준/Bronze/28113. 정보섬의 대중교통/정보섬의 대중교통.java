import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int a = readInt();
        int b = readInt();
        if (b == a) {
            System.out.println("Anything");
        } else if (b > a) {
            System.out.println("Bus");
        } else {
            System.out.println("Subway");
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