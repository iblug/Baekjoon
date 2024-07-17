import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int r = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        String h = br.readLine();
        for (int i = 0; i < n; i++) {
            if (Objects.equals(st.nextToken(), h)) {
                r++;
            }
        }
        System.out.println(r);
    }
}