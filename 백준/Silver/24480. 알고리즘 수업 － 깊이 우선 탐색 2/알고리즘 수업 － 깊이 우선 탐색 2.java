import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

    private static int[] visited;
    private static int cnt;
    private static List<List<Integer>> graph;
    private static StringBuilder sb;


    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), r = readInt();
        visited = new int[n + 1];
        graph = new ArrayList<>();
        sb = new StringBuilder();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        while (m-- > 0) {
            int u = readInt(), v = readInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        graph.forEach(node -> node.sort(Collections.reverseOrder()));

        dfs(r);

        for (int i = 1; i <= n; i++) {
            sb.append(visited[i]).append('\n');
        }
        System.out.println(sb);
    }

    private static void dfs(int x) {
        visited[x] = ++cnt;
        for (int i = 0; i < graph.get(x).size(); i++) {
            int v = graph.get(x).get(i);
            if (visited[v] == 0) {
                dfs(v);
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