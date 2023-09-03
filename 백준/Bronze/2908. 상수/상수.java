import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	private void solution() throws IOException {
		st = new StringTokenizer(br.readLine());
		String a = st.nextToken();
		String b = st.nextToken();
		
		char[] aa = new char[3];
		char[] bb = new char[3];
		
		for (int i = 0; i < 3; i++) {
			aa[i] = a.charAt(3-i-1);
			bb[i] = b.charAt(3-i-1);
		}
		
		int aaa = Integer.parseInt(new String(aa));
		int bbb = Integer.parseInt(new String(bb));
		
		System.out.println(Math.max(aaa, bbb));
	}
}