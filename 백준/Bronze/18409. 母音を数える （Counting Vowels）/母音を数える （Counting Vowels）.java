import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    final String[] e = new String[] {"a", "e", "i", "o", "u"};
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        br.readLine();
        String s = br.readLine();

        int r = 0;
        for (String v : e) {
            r += (int) s.chars()
                    .filter(i -> String.valueOf((char) i).equals(v))
                    .count();
        }
        System.out.println(r);
    }
}
