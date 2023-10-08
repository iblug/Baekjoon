import java.io.IOException;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		ArrayList<Integer> x = new ArrayList<>();
		ArrayList<Integer> y = new ArrayList<>();
		for (int i = 0; i < 3; i++) {
			int a = readInt();
			int b = readInt();
			if (x.contains(a)) {
				x.remove(x.indexOf(a));
			} else {
				x.add(a);
			}
			if (y.contains(b)) {
				y.remove(y.indexOf(b));
			} else {
				y.add(b);
			}
		}
		StringBuilder sb = new StringBuilder();
		sb.append(x.get(0)).append(" ").append(y.get(0));
		System.out.println(sb);
	}

	private int readInt() throws IOException {
		int v, t=0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return t;
		
	}
}
