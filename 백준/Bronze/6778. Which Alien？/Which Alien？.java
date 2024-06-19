import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int a = readInt();
        int e = readInt();

        StringBuilder sb = new StringBuilder();
        if (a >= 3 && e <= 4) {
            sb.append("TroyMartian\n");
        }
        if (a <= 6 && e >= 2) {
            sb.append("VladSaturnian\n");
        }
        if (a <= 2 && e <= 3) {
            sb.append("GraemeMercurian\n");
        }

        System.out.println(sb);
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