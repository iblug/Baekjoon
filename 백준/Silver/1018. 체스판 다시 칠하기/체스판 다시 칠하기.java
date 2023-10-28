import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		new Main().solution();
	}

	private void solution() throws Exception {
		int n = readInt();
		int m = readInt();

		int rw = 1000, rb = 1000;
		int w, b;
		String[] board = new String[n];
		for (int i = 0; i < n; i++) {
			board[i] = br.readLine();
		}
		for (int i = 0; i < n - 7; i++) {
			for (int j = 0; j < m - 7; j++) {
				w = 0;
				b = 0;
				for (int k = 0; k < 8; k++) {
					String s = board[i + k];
					for (int p = 0; p < 8; p++) {
						if (k % 2 == 0) {
							if (p % 2 == 0) {
								if (s.charAt(j + p) == 'B') {
									w++;
								} else {
									b++;
								}
							} else {
								if (s.charAt(j + p) == 'W') {
									w++;
								} else {
									b++;
								}								
							}
						} else {
							if (p % 2 == 0) {
								if (s.charAt(j + p) == 'W') {
									w++;
								} else {
									b++;
								}
							} else {
								if (s.charAt(j + p) == 'B') {
									w++;
								} else {
									b++;
								}								
							}
						}
							
					}

				}
				if (rw > w) {
					rw = w;
				}
				if (rb > b) {
					rb = b;
				}
			}
		}
		System.out.println(rw > rb? rb:rw);

	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}

}