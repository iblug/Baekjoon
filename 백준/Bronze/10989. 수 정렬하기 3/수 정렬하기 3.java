import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int[] a = new int[10001];
		for (int i = 0; i < n; i++) {
			a[readInt()]++;
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < 10001; i++) {
			if (a[i] > 0) {
				for (int j = 0; j < a[i]; j++) {
					sb.append(i).append("\n");
				}
			}
		}
		System.out.println(sb);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - '0');
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}
