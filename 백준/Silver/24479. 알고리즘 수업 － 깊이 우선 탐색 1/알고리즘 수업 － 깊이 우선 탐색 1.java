import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static boolean[] visited;
    public static ArrayList<ArrayList<Integer>> graph;
    public static StringBuilder sb;
    public static int[] nodes;
    public static int s;

    public static void dfs(int x) {
        visited[x] = true;
        nodes[x - 1] = s++;
        for (int i = 0; i < graph.get(x).size(); i++) {
            int v = graph.get(x).get(i);
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    private void solution() throws IOException {
        int n = readInt(), m = readInt(), r = readInt();
        graph = new ArrayList<>();
        visited = new boolean[n + 1];
        nodes = new int[n];
        sb = new StringBuilder();
        s = 1;
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

        Arrays.stream(nodes).forEach(node -> sb.append(node).append('\n'));
        System.out.println(sb);
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