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
		String result;
		if (x < 60) {
			result = "F";
		} else if (x < 70) {
			result = "D";
		} else if (x < 80) {
			result = "C";
		} else if (x < 90) {
			result = "B";
		} else {
			result = "A";
		}
		return result;
	}
}