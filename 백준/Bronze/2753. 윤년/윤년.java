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
		int N = Integer.parseInt(br.readLine());
		int isYoon = 0;
		if (N % 400 == 0) {
			isYoon = 1;
		} else if (N % 4 == 0) {
			if (N % 100 == 0) {
				isYoon = 0;
			} else {
				isYoon = 1;
			}
		}
		System.out.print(isYoon);
	}
}