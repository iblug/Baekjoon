import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = readInt();
        int a, b;

        StringBuilder sb = new StringBuilder();
        while (n-- > 0){
            a = readInt();
            b = readInt();
            if (a < b) {
                sb.append("NO BRAINS");
            } else {
                sb.append("MMM BRAINS");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }

        return t;
    }
}