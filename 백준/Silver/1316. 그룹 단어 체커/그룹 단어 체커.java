import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			boolean[] b = new boolean[26];
			boolean flag = true;
			String s = br.readLine();
			char pre = ' ';
			for (char c : s.toCharArray()) {
				if (c == pre) {
				} else {
					if (b[c - 97]) {
						flag = false;
						break;
					} else {
						b[c - 97] = true;
					}
				}
				pre = c;
			}
			if (flag) {
				cnt++;
			}
		}
		System.out.println(cnt);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}

}