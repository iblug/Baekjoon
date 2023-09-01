import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws Throwable {
		new Main().solution();
		br.close();
	}
	public void solution() throws IOException {
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			
			char[] c = st.nextToken().toCharArray();
			for (char e : c) {
				for (int j = 0; j < r; j++) {
					sb.append(e);
				}
			}
			sb.append('\n');
		}
		System.out.println(sb);
	}
}