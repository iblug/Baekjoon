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
	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		int max, min, t;
		StringTokenizer st = new StringTokenizer(br.readLine());
		max = min = Integer.parseInt(st.nextToken());
		for (int i = 1; i < n; i++) {
			t = Integer.parseInt(st.nextToken());
			if (t > max) {
				max = t;
			}
			if (t < min) {
				min = t;
			}
		}
		sb.append(min).append(" ").append(max);
		System.out.println(sb);
	}
}