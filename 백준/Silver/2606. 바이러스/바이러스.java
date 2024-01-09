import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static List<List<Integer>> graph;
    private static boolean[] visited;

    private static int cnt = 0;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        graph = new ArrayList<>();
        visited = new boolean[n+1];

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = readInt(), v = readInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        dfs(1);
        
        System.out.println(cnt - 1);
    }

    private static void dfs(int r) {
        visited[r] = true;
        cnt++;
        for (int i = 0; i < graph.get(r).size(); i++) {
            int v = graph.get(r).get(i);
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    private static int readInt() throws IOException {
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
