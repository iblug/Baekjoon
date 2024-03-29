import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Deque<String> q = new ArrayDeque<>();
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        while (n-- > 0) {
            if (st.nextToken().equals("0")) {
                q.offerLast(st2.nextToken());
            } else {
                st2.nextToken();
            }
        }
        int k = q.size();
        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            if (q.isEmpty()) {
                break;
            }
            sb.append(q.pollLast()).append(" ");
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m - k; i++) {
            sb.append(st.nextToken()).append(" ");
        }
        System.out.println(sb);
    }
}