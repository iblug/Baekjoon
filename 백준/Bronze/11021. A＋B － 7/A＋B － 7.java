import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	private void solution() throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int i = 1; i <= T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			System.out.printf("Case #%d: %d\n",i, Integer.parseInt(st.nextToken())+Integer.parseInt(st.nextToken()));
		}
	}
}