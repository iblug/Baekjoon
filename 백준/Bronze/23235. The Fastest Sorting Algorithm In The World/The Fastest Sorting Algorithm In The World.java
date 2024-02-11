import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        while (true) {
            st = new StringTokenizer(br.readLine());
            if (st.nextToken().equals("0")) {
                break;
            }
            sb.append("Case ").append(++cnt).append(": Sorting... done!\n");
        }
        System.out.println(sb);
    }
}