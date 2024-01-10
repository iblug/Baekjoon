import java.io.IOException;
import java.util.*;

public class Main {
    List<List<Integer>> graph;
    boolean[] visited;
    short cnt;
    StringBuilder sb;

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        sb = new StringBuilder();
        graph = new ArrayList<>();
        int n = readInt(), m = readInt(), r = readInt();
        visited = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int u = readInt(), v = readInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        graph.forEach(Collections::sort);

        dfs(r);
        sb.append('\n');

        cnt = 0;
        visited = new boolean[n + 1];

        bfs(r);

        System.out.println(sb);
    }

    void dfs(int r) {
        visited[r] = true;
        sb.append(r).append(' ');
        for (int i = 0; i < graph.get(r).size(); i++) {
            int v = graph.get(r).get(i);
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    void bfs(int r) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(r);
        visited[r] = true;
        sb.append(r).append(' ');
        while (!q.isEmpty()) {
            int c = q.poll();
            for (int i = 0; i < graph.get(c).size(); i++) {
                int v = graph.get(c).get(i);
                if (!visited[v]) {
                    q.offer(v);
                    visited[v] = true;
                    sb.append(v).append(' ');
                }
            }
        }
    }

    int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return t;
    }
}