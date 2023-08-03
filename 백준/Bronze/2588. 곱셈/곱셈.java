import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);

		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();
		
		sb.append(a * (b % 10));
		sb.append('\n');
		sb.append(a * ((b / 10) % 10));
		sb.append('\n');
		sb.append(a * ((b / 100) % 10));
		sb.append('\n');
		sb.append(a * b);
		
		System.out.println(sb);
	}

}