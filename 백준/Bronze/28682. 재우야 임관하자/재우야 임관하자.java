import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			sb.append("swimming ");
		}
		System.out.println(sb);
		System.out.flush();
		sb = new StringBuilder();
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			String t = st.nextToken();
			if (t.equals("bowling")) {
				sb.append("soccer ");
			} else if (t.equals("soccer")) {
				sb.append("bowling ");
			}
		}
		System.out.println(sb);
		System.out.flush();
	}
}