import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int n = readInt();
		int i = 1;
		while (true) {
			if (n <= i * (i -1) * 3 + 1) {
				break;
			}
			i++;
		}
		System.out.print(i);
	}
	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}
}
