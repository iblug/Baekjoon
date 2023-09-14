import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}

	private void solution() throws IOException {
		String[] d = new String[] { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
		String s = br.readLine();
		int a = 0;
		for (int i = 0; i < 8; i++) {
			a += count(s, d[i]);
		}
		System.out.println(s.length() - a);
	}

	public int count(String c, String s) {
		int cnt = 0;
		int index = 0;
		while ((index = c.indexOf(s, index)) != -1) {
			cnt++;
			index += s.length();
		}

		return cnt;
	}
}