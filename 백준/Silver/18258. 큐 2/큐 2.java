import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        Queue<String> q = new LinkedList<>();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "push":
                    q.offer(st.nextToken());
                    break;
                case "pop":
                    sb.append(q.isEmpty() ? "-1" : q.poll()).append("\n");
                    break;
                case "size":
                    sb.append(q.size()).append("\n");
                    break;
                case "empty":
                    sb.append(q.isEmpty() ? "1\n" : "0\n");
                    break;
                case "front":
                    sb.append(q.isEmpty() ? "-1" : q.peek()).append("\n");
                    break;
                case "back":
                    sb.append(q.isEmpty() ? "-1" : ((LinkedList<String>) q).peekLast()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}
