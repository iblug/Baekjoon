import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		String[] data = br.readLine().split(" ");
		long a = Long.parseLong(data[0]);
		long b = Long.parseLong(data[1]);
		long c = Long.parseLong(data[2]);
		System.out.println(a+b+c);
	}

}