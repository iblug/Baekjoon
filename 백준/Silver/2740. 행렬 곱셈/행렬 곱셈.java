import java.io.IOException;

public class Main {

    public static int[][] A, B;

    public static void main(String[] args) throws IOException {
        int N, M;
        N = readInt();
        M = readInt();
        A = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                A[i][j] = readInt();
            }
        }

        int K;
        M = readInt();
        K = readInt();
        B = new int[M][K];

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < K; j++) {
                B[i][j] = readInt();
            }
        }

        int[][] R = new int[N][K];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < K; j++) {
                for (int k = 0; k < M; k++) {
                    R[i][j] += A[i][k] * B[k][j];
                }
                sb.append(R[i][j]).append(' ');
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }


    private static int readInt() throws IOException {
        int v, t = 0;
        boolean f = false;
        while ((v = System.in.read()) > 32) {
            if (v == '-') {
                f = true;
                continue;
            }
            t = t * 10 + (v - 48);
        }
        if (v == 13) {
            System.in.read();
        }
        return f ? -t : t;
    }
}