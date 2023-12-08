import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String s = br.readLine();
		StringBuilder sb = new StringBuilder();
		sb.append(s.charAt(2)).append(s.charAt(1)).append(s.charAt(0));
		System.out.println(sb);
	}
}