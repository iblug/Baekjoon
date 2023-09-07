import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < 2 * n; i++) {
			if (i < n) {
				sb.append(" ".repeat(n - i)).append("*".repeat(2 * (i - 1) + 1));
			} else {
				sb.append(" ".repeat(i - n)).append("*".repeat(4 * n - 2 * i - 1));
			}
			sb.append("\n");
		}
		System.out.print(sb);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = 10 * t + (v - 48);
		}

		return t;
	}

}