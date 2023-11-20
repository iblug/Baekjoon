import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		long a = readLong();
		long b = readLong();
		System.out.println(a * b / getLcg(a, b));
		
	}

	private long getLcg(long a, long b) {
		if (a > b) {
			long t = a;
			a = b;
			b = t;
		}
		while (a > 0) {
			long t = a;
			a = b % a;
			b = t;
		}
		
		return b;
	}

	private long readLong() throws IOException {
		long v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}
}