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
		br.readLine();
		HashSet<String> set = new HashSet<>();
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			set.add(st.nextToken());
		}
		br.readLine();
		StringBuilder sb = new StringBuilder();
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			if (set.contains(st.nextToken())) {
				sb.append("1 ");
			} else {
				sb.append("0 ");
			}
		}
		System.out.println(sb);
	}
}
