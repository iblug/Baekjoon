import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int m = readInt();
        int d = readInt();
        if (m > 2) {
            System.out.println("After");
        } else if (m == 2 && d > 18) {
            System.out.println("After");
        } else if (m == 2 && d == 18) {
            System.out.println("Special");
        } else {
            System.out.println("Before");
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