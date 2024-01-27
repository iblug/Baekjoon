import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        LinkedList<String> q = new LinkedList<>();
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "1":
                    q.addFirst(st.nextToken());
                    break;
                case "2":
                    q.addLast(st.nextToken());
                    break;
                case "3":
                    sb.append(q.isEmpty() ? "-1" : q.pollFirst()).append("\n");
                    break;
                case "4":
                    sb.append(q.isEmpty() ? "-1" : q.pollLast()).append("\n");
                    break;
                case "5":
                    sb.append(q.size()).append("\n");
                    break;
                case "6":
                    sb.append(q.isEmpty() ? "1" : "0").append("\n");
                    break;
                case "7":
                    sb.append(q.isEmpty() ? "-1" : q.peekFirst()).append("\n");
                    break;
                case "8":
                    sb.append(q.isEmpty() ? "-1" : q.peekLast()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}