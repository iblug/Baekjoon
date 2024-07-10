import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        int n;
        while (t-- > 0) {
            n = Integer.parseInt(br.readLine());
            bw.write(String.valueOf(n));
            if (n % 2 != 0) {
                bw.write(" is odd\n");
            } else {
                bw.write(" is even\n");
            }
        }

        bw.flush();
        bw.close();
    }
}