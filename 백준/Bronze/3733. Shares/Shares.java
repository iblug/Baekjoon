import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		StringBuilder sb = new StringBuilder();
		while (true) {
			int a = readInt();
			if (a == 0) {
				break;
			}
			int b = readInt();
			sb.append(b / (a + 1)).append("\n");
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