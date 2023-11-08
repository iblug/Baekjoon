import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		HashSet<String> set = new HashSet<>();
		for (int i = 0; i < n; i++) {
			set.add(br.readLine());
		}
		List<String> list = new ArrayList<>(set);
		Collections.sort(list, (e1, e2) -> {
			if (e1.length() == e2.length()) {
				return e1.compareTo(e2);
			} else {
				return e1.length() - e2.length();
			}
		});
		
		StringBuilder sb = new StringBuilder();
		for (String e : list) {
			sb.append(e).append("\n");
		}
		System.out.println(sb);
	}
}