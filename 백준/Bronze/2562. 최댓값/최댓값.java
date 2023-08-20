import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] arg) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int m = 0, j = 0, t;
		for (int i = 1; i <= 9; i++) {
			t = Integer.parseInt(br.readLine());
			if (m < t) {
				m = t;
				j = i;
			}
		}
		StringBuilder sb = new StringBuilder();
		sb.append(m).append("\n").append(j);
		System.out.print(sb);
	}
}