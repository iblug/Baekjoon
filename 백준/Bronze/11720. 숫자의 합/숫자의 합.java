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
		char[] c = br.readLine().toCharArray();
		int r = 0;
		for (int i = 0; i < n; i++) {
			r += c[i] - '0';
		}
		System.out.println(r);
	}
}