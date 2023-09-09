import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		String g = br.readLine();
		float s = 0;
		for (int i = 0; i < g.length(); i++) {
			if (Character.isAlphabetic(g.charAt(i))) {
				switch (g.charAt(i)) {
				case 'A':
					s += 4;
					break;
				case 'B':
					s += 3;
					break;
				case 'C':
					s += 2;
					break;
				case 'D':
					s += 1;
					break;
				}				
			} else if (g.charAt(i) == '+') {
				s += 0.3;
			} else if (g.charAt(i) == '-') {
				s -= 0.3;
			}
		}
		System.out.print(s);
	}

}
