import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br;
    static int[][] graph;
    static int[] visited;
    static int N, K;

    static public void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        graph = new int[100001][];
        visited = new int[100001];
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        bfs(N);

        System.out.println(visited[K]);
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        while (!q.isEmpty()) {
            int c = q.poll();
            if (c == K) {
                break;
            }
            if (c - 1 >= 0 && visited[c - 1] == 0) {
                q.offer(c - 1);
                visited[c - 1] = visited[c] + 1;
            }
            if (c + 1 <= 100000 && visited[c + 1] == 0) {
                q.offer(c + 1);
                visited[c + 1] = visited[c] + 1;

            }
            if (c * 2 <= 100000 && visited[c * 2] == 0) {
                q.offer(c * 2);
                visited[c * 2] = visited[c] + 1;
            }
        }
    }
}