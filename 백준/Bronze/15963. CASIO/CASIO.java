import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        st = new StringTokenizer(br.readLine());
        String n = st.nextToken();
        String m = st.nextToken();
        if (n.equals(m)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}