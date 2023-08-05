import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int x = Integer.parseInt(br.readLine());
		int y = Integer.parseInt(br.readLine());
		
		System.out.print(getQ(x, y));
	}
	private int getQ(int x, int y) {
		if (x * y > 0) {
			if (x > 0) {
				return 1;
			} else {
				return 3;
			}
		} else {
			if (x < 0) {
				return 2;
			} else {
				return 4;
			}
		}
	}
}