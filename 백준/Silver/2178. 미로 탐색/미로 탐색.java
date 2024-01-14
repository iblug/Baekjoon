import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<String> graph;
    static boolean[][] visited;
    static final int[][] dxy = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    static int N, M;
    static BufferedReader br;

    public static void main(String[] args) throws IOException {
        N = readInt();
        M = readInt();
        graph = new ArrayList<>();
        visited = new boolean[N][M];
        br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < N; i++) {
            graph.add(br.readLine());
        }

        System.out.println(bfs(0, 0));

    }

    static int bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y, 1});
        visited[y][x] = true;
        while (!q.isEmpty()) {
            int[] nxy = q.poll();
            if (nxy[0] == M - 1 && nxy[1] == N - 1) {
                return nxy[2];
            }
            for (int i = 0; i < 4; i++) {
                int nx = nxy[0] + dxy[i][0];
                int ny = nxy[1] + dxy[i][1];

                if (nx < 0 || nx >= M || ny < 0 || ny >= N || visited[ny][nx]) {
                    continue;
                }

                if (graph.get(ny).charAt(nx) == '1') {
                    q.offer(new int[]{nx, ny, nxy[2] + 1});
                    visited[ny][nx] = true;
                }
            }
        }
        return -1;
    }

    static int readInt() throws IOException {
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