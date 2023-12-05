import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		StringBuilder sb = new StringBuilder();
		while (n-- > 0) {
			int a = readInt();
			int b = readInt();
			sb.append(a + b).append("\n");
		}
		System.out.println(sb);
		
	}

	private int readInt() throws IOException {
		int v, t = 0;
		boolean f = false;
		while ((v = System.in.read()) > 33) {
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