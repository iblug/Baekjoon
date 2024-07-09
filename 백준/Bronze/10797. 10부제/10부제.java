import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = 0;
        for(int i = 0; i < 5; i++) {
            if(n == Integer.parseInt(st.nextToken())) {
                r++;
            }
        }
        System.out.println(r);
    }
}
