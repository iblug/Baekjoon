import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        int n = Integer.parseInt(s);
        int r = 0;

        if (s.contains("7")) {
            r += 2;
        }

        if (n % 7 == 0) {
            r += 1;
        }

        System.out.println(r);
    }
}