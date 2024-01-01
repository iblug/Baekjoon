import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final List<Character> e = Arrays.asList('a', 'e', 'i', 'o', 'u');

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        int r = 0;
        for (int i = 0; i < n; i++) {
            if (e.contains(s.charAt(i))) {
                r++;
            }
        }

        System.out.println(r);
    }
}