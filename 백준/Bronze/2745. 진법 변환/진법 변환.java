import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		new Main().solution();
		br.close();
	}

	private void solution() throws IOException {
		st = new StringTokenizer(br.readLine());
		String s = st.nextToken();
		int b = Integer.parseInt(st.nextToken());
		int r = 0;
		for (int i = s.length() - 1; i >= 0; i--) {
			int c = 0;
			if (s.charAt(i) >= 65 && s.charAt(i) <= 97) {
				c = s.charAt(i) - 55;
			} else {
				c = s.charAt(i) - 48;
			}
			r += Math.pow(b, s.length() - i - 1) * c;
		}
		System.out.println(r);
	}

}