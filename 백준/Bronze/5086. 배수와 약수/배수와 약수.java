import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		StringBuilder sb = new StringBuilder();
		while (true) {
			int a = readInt();
			int b = readInt();
			if (a == 0 && b == 0) {
				break;
			}
			if (b % a == 0) {
				sb.append("factor\n");
			} else if (a % b == 0) {
				sb.append("multiple\n");
			} else {
				sb.append("neither\n");
			}
		}
		System.out.print(sb);
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