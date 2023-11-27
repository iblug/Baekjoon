import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String a = br.readLine();
		String b = br.readLine();
		
		if (a.length() < b.length()) {
			System.out.println("no");
		} else {
			System.out.println("go");			
		}
	}
}