import java.io.IOException;

public class Main {
	public static void main(String args[]) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			int c = readInt();
			sb.append(c / 25).append(" ");
			c %= 25;
			sb.append(c / 10).append(" ");
			c %= 10;
			sb.append(c / 5).append(" ").append(c % 5).append("\n");
		}
		System.out.print(sb);
	}

	private int readInt() throws IOException {
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