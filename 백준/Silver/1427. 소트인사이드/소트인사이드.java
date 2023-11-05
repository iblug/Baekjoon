import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String s = br.readLine();
		int n = s.length();
		char[] c = new char[n];
		for (int i = 0; i < n; i++) {
			c[i] = s.charAt(i);
		}
		Arrays.sort(c);
		StringBuilder sb = new StringBuilder();
		for (int i = n-1; i >= 0; i--) {
			sb.append(c[i]);
		}
		System.out.println(sb);
	}
}