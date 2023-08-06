import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		new Main().solution();
		br.close();
	}
	private void solution() throws IOException {
		StringBuilder sb = new StringBuilder();
		String[] data = br.readLine().split(" ");
		int a = Integer.parseInt(data[0]);
		int b = Integer.parseInt(data[1]);
		data = br.readLine().split(" ");
		int c = Integer.parseInt(data[0]);
		
		int t = (a * 60 + b)+c;
		a = t/60 < 24 ? t/60 : t/60 - 24; 
		sb.append(a).append(" ").append(t%60);
		System.out.println(sb);
	}
}