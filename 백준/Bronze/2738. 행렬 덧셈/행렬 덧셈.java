import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int m = readInt();
		
		int[][] A = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				A[i][j] += readInt();
			}
		}
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				sb.append(A[i][j] + readInt()).append(" ");
			}
			sb.append("\n");
		}
		
		System.out.print(sb);
		
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - '0');
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}