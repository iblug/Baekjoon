import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int N = readInt();
		int M = 0;
		int t;
		float s = 0;
		for (int i = 0; i < N; i++) {
			t = readInt();
			M = Math.max(M, t);
			s += t;
		}
		System.out.println(s/M/N*100);
		
	}
	private static int readInt() throws IOException {
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