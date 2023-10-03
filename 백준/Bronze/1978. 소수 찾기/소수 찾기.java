import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		boolean[] b = new boolean[1001];
		b[1] = true;
		for (int i = 2; i < 1001; i++) {
			if (!b[i]) {
				for (int j = i * 2; j < 1001; j += i) {
					b[j] = true;
				}
			}
		}
		int n = readInt();
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			int m = readInt();
			if (!b[m]) {
				cnt++;
			}
		}
		System.out.println(cnt);
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
