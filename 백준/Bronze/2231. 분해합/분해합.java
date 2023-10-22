import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int r = 0;
		for (int i = 0; i < n; i++) {
			int s = i;
			int k = 0;
			while (s > 0) {
				k += s % 10;
				s /= 10;
			}
			if (k == n - i) {
				r = i;
				break;
			}
		}
		System.out.println(r);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}
}