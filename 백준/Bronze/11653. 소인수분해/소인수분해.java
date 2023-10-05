import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		StringBuilder sb = new StringBuilder();
		while (n % 2 == 0) {
			sb.append(2).append("\n");
			n /= 2;
		}
		for (int i = 3; i <= n; i += 2) {
			while (n % i == 0) {
				sb.append(i).append("\n");
				n /= i;
			}
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
