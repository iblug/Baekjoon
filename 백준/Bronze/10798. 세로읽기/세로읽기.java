import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br;
	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		new Main().solution();
		br.close();
		
	}
	private void solution()  throws Exception {
		char[][] c = new char[5][];
		int max_length = 0;
		for (int i = 0; i < 5; i++) {
			String s = br.readLine();
			max_length = Math.max(max_length, s.length());
			c[i] = s.toCharArray();
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < max_length; i++) {
			for (int j = 0; j < 5; j++) {
				if (c[j].length > i) {
					sb.append(c[j][i]);
				}
			}
		}
		System.out.println(sb);
	}

}