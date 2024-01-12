import java.io.IOException;

public class Main {
    static boolean[][] graph;
    static int T, M, N, K, X, Y, cnt;
    static final int[] dx = {1, 0, -1, 0}, dy = {0, 1, 0, -1};
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        sb = new StringBuilder();
        T = readInt();
        while (T-- > 0) {
            M = readInt();
            N = readInt();
            K = readInt();
            graph = new boolean[N][M];
            cnt = 0;
            while (K-- > 0) {
                X = readInt();
                Y = readInt();
                graph[Y][X] = true;
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (graph[i][j]) {
                        dfs(i, j);
                        cnt++;
                    }
                }
            }
            sb.append(cnt).append('\n');
        }
        System.out.println(sb);
    }

    private static void dfs(int i, int j) {
        graph[i][j] = false;
        for (int d = 0; d < 4; d++) {
            int ny = i + dy[d];
            int nx = j + dx[d];
            if (nx < 0 || nx >= M || ny < 0 || ny >= N) {
                continue;
            }
            if (graph[ny][nx]) {
                dfs(ny, nx);
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