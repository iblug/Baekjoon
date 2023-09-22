import java.io.IOException;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		boolean[][] board = new boolean[101][101];
		int n = readInt();
		for (int i = 0; i < n; i++) {
			int a = readInt();
			int b = readInt();
			for (int j = 0; j < 10; j++) {
				for (int k = 0; k < 10; k++) {
					board[a + j][b + k] = true;
				}
			}
		}
		int cnt = 0;
		for (int i = 0; i <= 100; i++) {
			for (int j = 0; j <= 100; j++) {
				if (board[i][j]) {
					cnt++;
				}
			}
		}
		System.out.println(cnt);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = 10 * t + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}