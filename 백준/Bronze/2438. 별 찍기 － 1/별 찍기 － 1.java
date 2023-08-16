import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}

	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= n; i++) {
			sb.append("*".repeat(i)).append("\n");
		}
		System.out.println(sb);
	}
}
