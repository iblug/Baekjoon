import java.io.BufferedReader;
import java.io.IOException;

public class Main {
	static BufferedReader br;
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
	private void solution() throws IOException {
		int a, b;
		StringBuilder sb = new StringBuilder();
		while (true) {
			a = readInt();
			b = readInt();
			if (a == 0 && b == 0) {
				break;
			}
			if (a > b) {
				sb.append("Yes");
			} else {
				sb.append("No");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
	private int readInt() throws IOException {
		int v, t = 0;
		while((v = System.in.read()) > 47) {
			t = 10 * t + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}