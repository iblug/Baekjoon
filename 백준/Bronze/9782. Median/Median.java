import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t = 0;
        while (true) {
            t++;
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int s = 0;
            float r = 0;
            if (n == 0) {
                break;
            } else if (n % 2 == 1) {
                for (int i = 0; i < n; i++) {
                    s = Integer.parseInt(st.nextToken());
                    if (i == n/2) {
                        r = s;
                        break;
                    }
                }
            } else {
                for (int i = 0; i < n; i++) {
                    if (i == n/2) {
                        r = (float) (s + Integer.parseInt(st.nextToken()))/2;
                        break;
                    }
                    s = Integer.parseInt(st.nextToken());
                }
            }
            bw.write("Case ");
            bw.write(String.valueOf(t));
            bw.write(": ");
            bw.write(String.format("%.1f", r));
            bw.write('\n');
        }

        bw.flush();
        bw.close();
    }
}
