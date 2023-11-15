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
		br.readLine();
		HashMap<String, Integer> map = new HashMap<>();
		String s;
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			s = st.nextToken();
			if (map.containsKey(s)) {
				map.put(s, map.get(s) + 1);
			} else {
				map.put(s, 1);
			}
		}
		br.readLine();
		StringBuilder sb = new StringBuilder();
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			s = st.nextToken();
			if (map.containsKey(s)) {
				sb.append(map.get(s));
			} else {
				sb.append(0);
			}
			sb.append(" ");
		}
		System.out.println(sb);

	}
}