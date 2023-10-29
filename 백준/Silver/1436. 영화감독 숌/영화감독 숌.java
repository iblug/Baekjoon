import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solustion();
	}

	private void solustion() throws IOException {
		int n = readInt();
		int c = 1;
		int i = 666;
		String s = null;
		while (c != n) {
			i++;
			s = i + "";
			if (s.contains("666")) {
				c++;
			}
		}
		System.out.println(i);
	}
	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}
}