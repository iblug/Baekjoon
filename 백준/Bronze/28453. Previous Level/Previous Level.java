import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	public void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int a = Integer.parseInt(st.nextToken());
			if (a < 250) {
				sb.append(4).append(" ");
			} else if (a < 275) {
				sb.append(3).append(" ");
			} else if (a < 300) {
				sb.append(2).append(" ");
			} else {
				sb.append(1).append(" ");
			}
		}
		System.out.println(sb);
	}
}