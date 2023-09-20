import java.io.FileInputStream;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	static StringTokenizer st;

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		int m = 0;
		int x = 0, y = 0;
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
				int t = readInt();
				if (t >= m) {
					x = i;
					y = j;
					m = t;
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		sb.append(m).append('\n').append(x).append(' ').append(y);

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