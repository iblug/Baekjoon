import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		List<Integer> a = new ArrayList<>();
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			a.add(Integer.parseInt(st.nextToken()));
		}
		List<Integer> list = new ArrayList<>(new HashSet<>(a));
		Collections.sort(list);
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < list.size(); i++) {
			map.put(list.get(i), i);
		}
		StringBuilder sb = new StringBuilder();
		for (int i : a) {
			sb.append(map.get(i)).append(" ");
		}
		System.out.println(sb);
	}
}
