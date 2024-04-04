import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int s = 0;
        while (n-- > 0) {
            s += Integer.parseInt(br.readLine());
        }

        System.out.println(s);
    }
}