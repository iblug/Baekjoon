import java.io.IOException;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		StringBuilder sb = new StringBuilder();
		sb.append(readInt()).append("\n1");
        System.out.print(sb);
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}

}