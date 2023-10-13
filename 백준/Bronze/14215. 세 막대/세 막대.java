import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

	private void solution() throws IOException {
		ArrayList<Integer> arr = new ArrayList<>();
		arr.add(readInt());
		arr.add(readInt());
		arr.add(readInt());
		Collections.sort(arr);
		if (arr.get(0) + arr.get(1) <= arr.get(2)) {
			System.out.println((arr.get(0) + arr.get(1)) * 2 - 1);
		} else {
			System.out.println(arr.get(0) + arr.get(1) + arr.get(2));
		}
	}

	private int readInt() throws IOException {
		int v, t = 0;
		while ((v = System.in.read()) > 47) {
			t = t * 10 + (v - 48);
		}
		return t;
	}

}