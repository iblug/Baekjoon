import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        int r = 0;
        char c;
        for (int i = 0; i < n; i++) {
            c = s.charAt(i);
            if (c == 'i' || c == 'j') {
                r += 2;
            } else {
                r++;
            }
        }
        System.out.println(r);
    }
}