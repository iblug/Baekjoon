import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	private BufferedReader sb = new BufferedReader(new InputStreamReader(System.in));
	private StringTokenizer st;
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
	
	private void solution() throws Exception {
		st = new StringTokenizer(sb.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());
		int f = Integer.parseInt(st.nextToken());
		
		int y = (a*f-d*c)/(a*e-b*d);
		StringBuilder sb = new StringBuilder();
		if (a == 0) {
			int x = (f-e*y)/d;
			sb.append(x);
		} else {
			int x = (c-b*y)/a;
			sb.append(x);
		}
		sb.append(' ').append(y);
		
		System.out.println(sb);
	}

}