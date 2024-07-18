import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean f, r = true;
        for (int i = 0; i < 3; i++) {
            f = false;
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                if (Objects.equals(st.nextToken(), "7")) {
                    f = true;
                    break;
                }
            }
            if (!f) {
                r = false;
                break;
            }
        }

        System.out.println(r ? 777 : 0);
    }
}