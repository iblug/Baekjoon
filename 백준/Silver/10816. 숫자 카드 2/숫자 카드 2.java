import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int[] a = new int[20000001];
		int i;
		while (n-- > 0) {
			i = readInt();
			a[i+10000000]++;
		}
		n = readInt();
		StringBuilder sb = new StringBuilder();
		while (n-- > 0) {
			i = readInt();
			sb.append(a[i+10000000]).append(" ");
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
		return f? -t : t;
	}
}