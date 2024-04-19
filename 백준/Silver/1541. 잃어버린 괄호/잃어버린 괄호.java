import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = Integer.MAX_VALUE;

        StringTokenizer st1 = new StringTokenizer(br.readLine(), "-");
        while (st1.hasMoreTokens()) {
            int n = 0;

            StringTokenizer st2 = new StringTokenizer(st1.nextToken(), "+");

            while (st2.hasMoreTokens()) {
                n += Integer.parseInt(st2.nextToken());
            }

            if (result == Integer.MAX_VALUE) {
                result = n;
            } else {
                result -= n;
            }
        }

        System.out.println(result);
    }
}