import java.io.IOException;

public class Main {
	public static void main(String args[]) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int n = readInt();
		int s = 0, i = 0;
		while (true) {
			i += 1;
			s += i;
			if (n <= s) {
				break;
			}
		}
		if (i % 2 == 0) {
			System.out.printf("%d/%d", i-s+n, s-n+1);
		} else {
			System.out.printf("%d/%d", s-n+1, i-s+n);
		}
	}
	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}
}