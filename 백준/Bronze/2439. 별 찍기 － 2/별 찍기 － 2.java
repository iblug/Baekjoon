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
		String str = " ";
		for (int i = 0; i < n; i++) {
			str = " ";
			for (int j = 0; j < n; j++) {
				if (j == n-i-1) {
					str = "*";
				}
				sb.append(str);
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}
