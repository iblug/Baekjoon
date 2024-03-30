import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        boolean b = false;
        for (int i = 0; i < 8; i++) {
            if (readInt() == 9) {
                b = true;
                break;
            }
        }
        if (b) {
            System.out.println("F");
        } else {
            System.out.println("S");
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