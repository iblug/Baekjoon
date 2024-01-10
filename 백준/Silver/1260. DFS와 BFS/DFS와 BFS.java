import java.io.IOException;
import java.util.*;

public class Main {
    private static List<List<Integer>> graph;
    private static boolean[] visited;
    private static StringBuilder sb;

    public static void main(String[] args) throws IOException {
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

        visited = new boolean[n + 1];

        bfs(r);

        System.out.println(sb);
    }

    private static void dfs(int r) {
        visited[r] = true;
        sb.append(r).append(' ');
        for (int i = 0; i < graph.get(r).size(); i++) {
            int v = graph.get(r).get(i);
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    private static void bfs(int r) {
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

    private static int readInt() throws IOException {
        int t = 0;
        byte v;
        while ((v = read()) <= 32);
        do t = (t << 3) + (t << 1) + (v & 15);
        while (isNumber(v = read()));
        return t;
    }

    static final int SIZE = 1 << 13;
    static byte[] buffer = new byte[SIZE];
    static int index, size;
    private static byte read() throws IOException {
        if (index == size) {
            size = System.in.read(buffer, index = 0, SIZE);
            if (size < 0) buffer[0] = -1;
        }
        return buffer[index++];
    }

    static boolean isNumber(byte c) {
        return 47 < c && c < 58;
    }
}