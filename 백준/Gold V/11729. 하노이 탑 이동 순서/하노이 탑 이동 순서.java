import java.io.*;

public class Main {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        bw.write(String.valueOf((int) Math.pow(2, n) - 1));
        bw.write('\n');

        hanoi(n, '1', '2', '3');

        bw.flush();
        bw.close();
    }

    static void hanoi(int n, char s, char m, char e) throws IOException {
        if (n == 1) {
            bw.write(s);
            bw.write(' ');
            bw.write(e);
            bw.write('\n');
            return;
        }
        hanoi(n - 1, s, e, m);
        bw.write(s);
        bw.write(' ');
        bw.write(e);
        bw.write('\n');
        hanoi(n - 1, m, s, e);
    }
}