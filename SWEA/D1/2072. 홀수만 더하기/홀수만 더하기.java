import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		new Solution().solution();
		br.close();
	}

	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		for (int i = 1; i <= n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int sum = 0;
			for (int j = 0; j < 10; j++) {
				int a = Integer.parseInt(st.nextToken());
				if ((a & 1) == 1) {
					sum += a;
				}
			}
			sb.append("#").append(i).append(" ").append(sum).append("\n");
		}
		System.out.print(sb);
	}
}