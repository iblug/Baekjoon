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
		int[] c = new int[26];
		String s = br.readLine();
		s = s.toUpperCase();
		for (int i = 0; i < s.length(); i++) {
			c[s.charAt(i) - 'A'] += 1;
		}
		int m = -1;
		boolean f = true;
		int t = -1;
		for (int i = 0; i < c.length; i++) {
			if (c[i] > m) {
				m = c[i];
				t = i;
				f = true;
			} else if (c[i] == m) {
				f = false;
			}
		}

		if (f) {
			System.out.println((char) (t + 'A'));
		} else {
			System.out.println('?');
		}
	}
}