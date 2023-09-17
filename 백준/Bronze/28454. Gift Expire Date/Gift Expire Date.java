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
		StringTokenizer st = new StringTokenizer(br.readLine(), "-");
		int y = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		
		int n = Integer.parseInt(br.readLine());

		int c = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine(), "-");
			int g_y = Integer.parseInt(st.nextToken());
			int g_m = Integer.parseInt(st.nextToken());
			int g_d = Integer.parseInt(st.nextToken());			
			
			if (g_y > y) {
				c++;
			} else if (g_y == y && g_m > m) {
				c++;
			} else if (g_y == y && g_m == m && g_d >= d) {
				c++;
			}
		}
		System.out.print(c);
	}
}