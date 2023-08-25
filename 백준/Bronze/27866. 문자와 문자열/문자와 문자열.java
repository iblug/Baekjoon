import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		String s = br.readLine();
		int n = Integer.parseInt(br.readLine());
		
		System.out.println(s.charAt(n-1));
	}
}