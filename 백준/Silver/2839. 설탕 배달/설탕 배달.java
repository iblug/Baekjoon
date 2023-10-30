import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int a = readInt();
		int c = 0;
		while (a > 0) {
			if (a % 5 == 0) {
				c += a / 5;
				break;
			} else if (a < 3) {
				c = -1;
				break;
			}
			a -= 3;
			c++;
		}
		System.out.println(c);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}
}