import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n;
		StringBuilder sb = new StringBuilder();
		while (true) {
			n = readInt();
			if (n == 0) {
				break;
			}
			sb.append(n * (n + 1) / 2).append("\n");
		}
		System.out.println(sb);
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