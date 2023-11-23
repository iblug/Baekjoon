import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		long n = readLong();
		while (n-- > 0) {
			long a = readLong();
			while (true) {
				if (isPrime(a)) {
					System.out.println(a);
					break;
				} else {
					a++;
				}
			}
		}
	}

	private long readLong() throws IOException {
		int v;
		long t = 0;
		while ((v = System.in.read()) >= '0') {
			t = t * 10 + (v - '0');
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}

	private boolean isPrime(long x) {
		if (x == 0 || x == 1) {
			return false;
		}
		for (int i = 2; i < Math.floor(Math.sqrt(x)) + 1; i++) {
			if (x % i == 0) {
				return false;
			}
		}
		return true;
	}
}