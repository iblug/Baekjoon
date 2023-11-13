import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		HashSet<String> set = new HashSet<>();
		String name = null;
		String type = null;

		StringTokenizer st;
		while (n-- > 0) {
			st = new StringTokenizer(br.readLine());
			name = st.nextToken();
			type = st.nextToken();
			if (type.startsWith("l") && set.contains(name)) {
				set.remove(name);
			} else if (type.startsWith("e")) {
				set.add(name);
			}
		}
		List<String> list = new ArrayList<>(set);
		Collections.sort(list, (e1, e2) -> {
			return e2.compareTo(e1);
		});
		StringBuilder sb = new StringBuilder();
		for (String s : list) {
			sb.append(s).append("\n");
		}
		System.out.println(sb);
	}
}