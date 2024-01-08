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

        graph.forEach(node -> node.sort(Collections.reverseOrder()));

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