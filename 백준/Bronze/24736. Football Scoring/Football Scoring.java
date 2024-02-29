import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = 0;
        s += 6 * Integer.parseInt(st.nextToken());
        s += 3 * Integer.parseInt(st.nextToken());
        s += 2 * Integer.parseInt(st.nextToken());
        s += Integer.parseInt(st.nextToken());
        s += 2 * Integer.parseInt(st.nextToken());
        sb.append(s).append(' ');

        st = new StringTokenizer(br.readLine());
        s = 0;
        s += 6 * Integer.parseInt(st.nextToken());
        s += 3 * Integer.parseInt(st.nextToken());
        s += 2 * Integer.parseInt(st.nextToken());
        s += Integer.parseInt(st.nextToken());
        s += 2 * Integer.parseInt(st.nextToken());
        sb.append(s);

        System.out.println(sb);
    }
}
