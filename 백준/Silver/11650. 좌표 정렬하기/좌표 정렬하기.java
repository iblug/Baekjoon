import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int[][] a = new int[n][2];
		for (int i = 0; i < n; i++) {
			a[i][0] = readInt();
			a[i][1] = readInt();
		}
		Arrays.sort(a, (e1, e2) -> {
			if (e1[0] == e2[0]) {
				return e1[1] - e2[1];
			} else {
				return e1[0] - e2[0];
			}
		});
		StringBuilder sb = new StringBuilder();
		for (int[] e : a) {
			sb.append(e[0]).append(" ").append(e[1]).append("\n");
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
			t = t * 10 + (v - '0');
		}
		if (v == 13) {
			System.in.read();
		}
		return f ? -t : t;
	}
}
