import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            sb.append(c(readInt(), readInt(), readInt(), readInt(), readInt(), readInt())).append('\n');
        }

        System.out.println(sb);
    }

    static String c(int h1, int m1, int s1, int h2, int m2, int s2) {
        StringBuilder sb = new StringBuilder();
        int t1 = h1*3600 + m1*60 + s1;
        int t2 = h2*3600 + m2*60 + s2;
        int t3 = t2 - t1;
        return sb.append(t3/3600).append(' ').append(t3%3600/60).append(' ').append(t3%3600%60).toString();
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