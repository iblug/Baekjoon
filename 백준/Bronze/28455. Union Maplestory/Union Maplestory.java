import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	public void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		Integer[] d = new Integer[n];
		for (int i = 0; i < n; i++) {
			d[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(d, Collections.reverseOrder());
		int m = n >= 42 ? 42 : n;
		int s = 0, c = 0;
		for (int i = 0; i < m; i++) {
			int a = d[i];
			s += a;
			if (a >= 250) {
				c += 5;
			} else if (a >= 200) {
				c += 4;
			} else if (a >= 140) {
				c += 3;
			} else if (a >= 100) {
				c += 2;
			} else if (a >= 60) {
				c++;
			}
		}
		sb.append(s).append(' ').append(c);
		System.out.print(sb);
	}
}