import java.io.IOException;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int m = readInt();
		HashSet<Integer> a = new HashSet<>();
		HashSet<Integer> b = new HashSet<>();
		while (n-- > 0) {
			a.add(readInt());
		}
		while (m-- > 0) {
			b.add(readInt());
		}
		HashSet<Integer> t = new HashSet<>(a);
		
		a.removeAll(b);
		b.removeAll(t);
		a.addAll(b);
		
		System.out.println(a.size());
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) >= '0') {
			t = t * 10 + (v - '0');
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}