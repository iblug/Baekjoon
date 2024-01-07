import java.io.IOException;
import java.util.*;

public class Main {
    private static List<List<Integer>> graph;
    private static int[] visited;
    private static int cnt;
    private static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        sb = new StringBuilder();
        int n = readInt(), m = readInt(), r = readInt();
        visited = new int[n + 1];
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = readInt(), v = readInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        graph.forEach(Collections::sort);

        bfs(r);

        for (int i = 1; i <= n; i++) {
            sb.append(visited[i]).append('\n');
        }

        System.out.println(sb);
    }

    private static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = ++cnt;

        while (!queue.isEmpty()) {
            int x = queue.poll();
            for (int i = 0; i < graph.get(x).size(); i++) {
                int y = graph.get(x).get(i);
                if (visited[y] == 0) {
                    queue.offer(y);
                    visited[y] = ++cnt;
                }
            }
        }
    }

    private static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = 10 * t + v - 48;
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}
