import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String s = br.readLine();

		StringBuilder sb = new StringBuilder();
		for (int i = 'a'; i < 'z' + 1; i++) {
			sb.append(s.indexOf(i)).append(" ");
		}
		System.out.print(sb);
	}
}