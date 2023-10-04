import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int m = readInt();
		int mn = m - n + 1;
		boolean[] b = new boolean[mn]; 
		if (n == 1) {
			b[0] = true;
		}

		for (int i = 2; i * i <= m; i++) { 
			int start = Math.max(i * i, ((n + i - 1) / i) * i); 
			for (int j = start; j <= m; j += i) { 
				if (j != i && j >= n) {
					b[j - n] = true;
				}
			}

		}
		int min = -1;
		int s = 0;
		for (int i = 0; i < mn; ++i) {
			if (!b[i]) {
				s += i + n;
				if (min == -1) {
					min = i + n;
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		if (min != -1) {
			sb.append(s).append("\n").append(min);
		} else {
			sb.append(min);
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