import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int[] d = new int[n];
		for (int i = 0; i < n; i++) {
			d[i] = readInt();
		}
		Arrays.sort(d);
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			sb.append(d[i]).append('\n');
		}
		System.out.println(sb);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		boolean f = false;
		while ((v = System.in.read()) > 32) {
			if (v == 45) {
				f = true;
				continue;
			}
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return f?-t:t;
	}
}