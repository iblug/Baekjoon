import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int c = 0;

		HashSet<String> s = new HashSet<>();
		while (n-- >0) {
			s.add(br.readLine());
		}
		while (m-- > 0) {
			if (s.contains(br.readLine())) {
				c++;
			}
		}
		System.out.println(c);
	}
}
