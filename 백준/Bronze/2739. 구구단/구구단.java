import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int N = Integer.parseInt(br.readLine());
		for (int i = 1; i <= 9; i++) {
			sb.append(N).append(" * ").append(i).append(" = ").append(N * i).append("\n");
		}
		System.out.println(sb);
	}
}