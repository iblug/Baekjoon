import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	private void solution()	throws IOException {
		int n = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		int t = Integer.parseInt(br.readLine());
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			if (t == Integer.parseInt(st.nextToken())) {
				cnt++;
			}
		}
		System.out.println(cnt);
	}
}