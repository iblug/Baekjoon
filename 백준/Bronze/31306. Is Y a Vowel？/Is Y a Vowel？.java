import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] a = br.readLine().toCharArray();
        char[] m = {'a', 'e', 'i', 'o', 'u'};
        int r = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < a.length; j++) {
                if (m[i] == a[j]) {
                    r++;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(r).append(' ');
        for (int i = 0; i < a.length; i++) {
            if ('y' == a[i]) {
                r++;
            }
        }
        sb.append(r);

        System.out.println(sb);
    }
}