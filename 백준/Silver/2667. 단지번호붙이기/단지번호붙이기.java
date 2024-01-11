import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static List<String> graph;
    static boolean[][] visited;
    static BufferedReader br;
    static int cnt, dCnt, N;
    static final int[] dx = {0, 0, -1, 1}, dy = {-1, 1, 0, 0};
    static List<Integer> result;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        N = readInt();
        graph = new ArrayList<>();
        visited = new boolean[N][N];
        result = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            graph.add(br.readLine());
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dCnt = 0;
                char c = graph.get(i).charAt(j);
                if (c == '1' && !visited[i][j]) {
                    cnt++;
                    dfs(i, j);
                    result.add(dCnt);
                }
            }
        }

        Collections.sort(result);
        sb = new StringBuilder();
        sb.append(cnt).append('\n');
        for (int i : result) {
            sb.append(i).append('\n');
        }
        System.out.println(sb);
    }

    private static void dfs(int r, int c) {
        visited[r][c] = true;
        dCnt++;
        for (int d = 0; d < 4; d++) {
            int y = r + dy[d];
            int x = c + dx[d];
            if (y < 0 || y >= N || x < 0 || x >= N) {
                continue;
            }
            char a = graph.get(y).charAt(x);
            if (a == '1' && !visited[y][x]) {
                dfs(y, x);
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