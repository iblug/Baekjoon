import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	private void solution() throws IOException {
		while (true) {
			char[] d = br.readLine().toCharArray();
			if (d[0] == '0' && d[2] == '0') {
				break;
			} else {
				sb.append(Character.getNumericValue(d[0]) + Character.getNumericValue(d[2])).append('\n');
			}
		}
		System.out.println(sb);
	}
}