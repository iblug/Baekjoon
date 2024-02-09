import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());
        System.out.println(f(n));
    }
    static long f(long n) {
        if (n == 0) {
            return 0;
        }
        if (n < 3) {
            return 1;
        }
        return f(n - 1) +  f(n - 2);
    }
}