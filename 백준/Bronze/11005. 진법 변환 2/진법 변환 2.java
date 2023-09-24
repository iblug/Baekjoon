import java.io.IOException;

public class Main {

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int b = readInt();
		StringBuilder sb = new StringBuilder();
		while (n > 0) {
			int t = n % b;
			if (t > 9) {
				char c = (char) (n % b - 10 + 'A');
				sb.append(c);
			} else {
				sb.append(t);
			}
			n = n / b;

		}
		sb.reverse();
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