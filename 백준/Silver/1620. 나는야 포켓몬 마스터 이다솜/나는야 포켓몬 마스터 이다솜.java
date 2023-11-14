import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		st = new StringTokenizer(br.readLine());
		HashMap<String, Integer> map = new HashMap<>();
		HashMap<Integer, String> map2 = new HashMap<>();

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i <= n; i++) {
			String s = br.readLine();
			map.put(s, i);
			map2.put(i, s);
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < m; i++) {
			String s = br.readLine();
			if (Character.isDigit(s.charAt(0))) {
				int t = Integer.parseInt(s);
				sb.append(map2.get(t));
			} else {
				sb.append(map.get(s));
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}