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
		int X = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int s = 0;
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			s += a*b;
		}
		if (s == X) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}