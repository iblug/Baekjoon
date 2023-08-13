import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	void solution() throws IOException {
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n/4; i++) {
			sb.append("long ");
		}
		sb.append("int");
		System.out.println(sb);
	}
}