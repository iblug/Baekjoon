import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().solution();
	}

	private void solution() throws IOException {
		int n = readInt();
		int minX, minY, maxX, maxY;
		minX = minY = 10000;
        maxX = maxY = -10000;
		for (int i = 0; i < n; i++) {
			int x = readInt();
			int y = readInt();
			if (minX > x) minX = x;
            if (minY > y) minY = y;
            if (maxX < x) maxX = x;
            if (maxY < y) maxY = y;
		}
		System.out.println((maxX - minX) * (maxY - minY));
	}

	private int readInt() throws IOException {
		int v, t = 0;
		boolean neg = false;
		while ((v = System.in.read()) > 33) {
			if (v == 45) {
				neg = true;
				continue;
			}
			t = t * 10 + (v - 48);
		}
		if (v == 13) {
			System.in.read();
		}
		return neg? -t:t;
	}

}