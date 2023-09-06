import java.io.IOException;

public class Main {
	static int[] m = new int[] { 1, 1, 2, 2, 2, 8 };

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 6; i++) {
			sb.append(m[i] - readInt()).append(" ");
		}
		System.out.println(sb);
	}

	private int readInt() throws IOException {
		int v, t = 0;

		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}

}