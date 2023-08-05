import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int a = Integer.parseInt(br.readLine());
		System.out.print(getGrade(a));
	}
	private String getGrade(int x) {
		if (x < 60) {
			return "F";
		} else if (x < 70) {
			return "D";
		} else if (x < 80) {
			return "C";
		} else if (x < 90) {
			return "B";
		} else {
			return "A";
		}
	}
}