import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        int a = readInt();
        int b = readInt();
        int c = readInt();
        int d = readInt();

        int t = (a * 3600 + b * 60 + c + d) % (3600 * 24);

        StringBuilder sb = new StringBuilder();
        sb.append(t / 3600).append(' ').append((t % 3600) / 60).append(' ').append(t % 3600 % 60);
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