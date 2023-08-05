import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String[] data = br.readLine().split(" ");
		int H = Integer.parseInt(data[0]);
		int M = Integer.parseInt(data[1]);
		br.close();
		StringBuilder sb = new StringBuilder();
		
		int h = H * 60 + M - 45;
		if (h < 0) {
			h += 24*60;
		}
		sb.append(h/60).append(" ").append(h%60);
		System.out.println(sb);
	}
}