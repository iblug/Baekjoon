import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        st = new StringTokenizer(br.readLine());
        System.out.println(((Integer.parseInt(st.nextToken()) + 1) * (Integer.parseInt(st.nextToken()) + 1) / (Integer.parseInt(st.nextToken()) + 1)) - 1);
    }
}