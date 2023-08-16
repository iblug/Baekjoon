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
		String s;
		while ((s = br.readLine()) != null) {
			sb.append(Character.getNumericValue(s.charAt(0)) + Character.getNumericValue(s.charAt(2))).append("\n");
		}
		System.out.print(sb);
	}
}