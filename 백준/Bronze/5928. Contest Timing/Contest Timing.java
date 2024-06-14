import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int t = (readInt()-11)*1440+(readInt()-11)*60+readInt()-11;
        System.out.println(t < 0 ? -1 : t);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}