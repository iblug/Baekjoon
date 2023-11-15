import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		br.readLine();
		int[] a = new int[20000001];
		int i;
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			i = Integer.parseInt(st.nextToken());
			a[i+10000000]++;
		}
		br.readLine();
		StringBuilder sb = new StringBuilder();
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			i = Integer.parseInt(st.nextToken());
			sb.append(a[i+10000000]).append(" ");
		}
		System.out.println(sb);

	}
}