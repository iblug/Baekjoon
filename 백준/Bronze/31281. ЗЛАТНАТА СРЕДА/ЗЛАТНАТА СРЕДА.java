import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        BigInteger[] a = new BigInteger[3];
        for (int i = 0; i < 3; i++) {
            a[i] = new BigInteger(st.nextToken());
        }
        Arrays.sort(a);
        System.out.println(a[1]);
    }
}