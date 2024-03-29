import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int a = readInt();
		int b = readInt();
		int v = readInt();
		int cnt = (int) Math.ceil((double) (v - a) / (a - b));
		System.out.println(cnt + 1);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}

}
