import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean[] f = new boolean[10];
        int a;
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            f[Integer.parseInt(st.nextToken())] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            if (f[i]) {
                sb.append(i).append("\n");
            }
        }

        System.out.println(sb);
    }
}