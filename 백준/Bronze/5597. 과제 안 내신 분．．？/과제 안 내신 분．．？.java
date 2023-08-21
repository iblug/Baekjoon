import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) throws IOException {
		new Main().solution();
	}
	private void solution() throws IOException {
		int i;
		HashSet<Integer> set = new HashSet<Integer>();
//		int[] arr = new int[30];
		for (i = 1; i <= 30; i++) {
			set.add(i);
		}
		for (i = 0; i < 28; i++) {
			set.remove(readInt());
		}
		ArrayList<Integer> arr = new ArrayList<>(set);
		Collections.sort(arr);
		StringBuilder sb = new StringBuilder();
		for (i = 0; i < 2; i++) {
			sb.append(arr.get(i)).append("\n");
		}
		System.out.println(sb);
		
	}
	private static int readInt() throws IOException {
		int v, t = System.in.read() & 15;
		while ((v = System.in.read()) > 32)
			t = (t << 3) + (t << 1) + (v & 15);
		if (v == 13) {
			System.in.read();
		}
		return t;
	}
}