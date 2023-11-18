import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String s = br.readLine();
		HashSet<String> set = new HashSet<>();
		int c = 0;
		for (int i = 0; i < s.length(); i++) {
			for (int j = i + 1; j < s.length() + 1; j++) {
				String t = s.substring(i, j);
				if (!set.contains(t)) {
					set.add(t);
					c++;
				}
			}
		}
		System.out.println(c);
	}
}