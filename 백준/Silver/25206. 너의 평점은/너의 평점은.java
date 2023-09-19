import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));		
		new Main().solution();
		br.close();
	}
	private void solution() throws IOException {
		float s = 0;
		float sh = 0;
		for (int i = 0; i < 20; i++) {
			st = new StringTokenizer(br.readLine());
			st.nextToken();
			float h = Float.parseFloat(st.nextToken());		
			String grade = st.nextToken();
			switch (grade) {
			case "A+":
				s += 4.5 * h;
				sh += h;
				break;
			case "A0":
				s += 4.0 * h;
				sh += h;
				break;
			case "B+":
				s += 3.5 * h;
				sh += h;
				break;
			case "B0":
				s += 3.0 * h;
				sh += h;
				break;
			case "C+":
				s += 2.5 * h;
				sh += h;
				break;
			case "C0":
				s += 2.0 * h;
				sh += h;
				break;
			case "D+":
				s += 1.5 * h;
				sh += h;
				break;
			case "D0":
				s += 1.0 * h;
				sh += h;
				break;
			case "F":
				sh += h;
				break;
			case "P":
				break;
			}
		}
		System.out.println(s/sh);
	}

}