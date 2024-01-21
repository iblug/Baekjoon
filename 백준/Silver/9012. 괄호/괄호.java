import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (n-- > 0) {
            String bs = br.readLine();
            boolean f = true;
            while (!bs.isEmpty()) {
                String b = bs.replace("()", "");
                if (b.equals(bs)) {
                    f = false;
                    break;
                }
                bs = b;
            }
            sb.append(f ? "YES" : "NO").append("\n");
        }
        System.out.println(sb);
    }
}