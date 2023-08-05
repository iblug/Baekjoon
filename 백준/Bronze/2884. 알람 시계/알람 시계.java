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
		String[] data = br.readLine().split(" ");
		int H = Integer.parseInt(data[0]);
		int M = Integer.parseInt(data[1]);

		if (M < 45) {
			M += 15;
			if (H == 0) {
				H = 23;
			} else {
				H--;
			}
		} else {
			M -= 45;
		}
		System.out.print(H + " " + M);	
	}
}