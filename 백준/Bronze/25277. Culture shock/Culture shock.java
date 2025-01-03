import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static String[] words = {"he", "him", "she", "her"};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int r = 0;
        for (int i = 0; i < n; i++) {
            if (Arrays.asList(words).contains(st.nextToken())) {
                r++;
            }
        }

        System.out.println(r);
    }
}