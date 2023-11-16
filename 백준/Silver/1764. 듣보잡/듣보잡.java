import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		HashSet<String> set = new HashSet<>();
		HashSet<String> set2 = new HashSet<>();
		while (n-- > 0) {
			set.add(br.readLine());
		}
		while (m-- > 0) {
			String s = br.readLine();
			if (set.contains(s)) {
				set2.add(s);
			}
		}
		ArrayList<String> list = new ArrayList<>(set2);
		Collections.sort(list);
		StringBuilder sb = new StringBuilder();
		
		sb.append(list.size());
		for (String s : list) {
			sb.append("\n").append(s);
		}
		System.out.println(sb);
	}
}