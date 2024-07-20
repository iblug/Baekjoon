import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = "123456789";
        String n = br.readLine();
        if (a.startsWith(n)) {
            System.out.println(n.length());
        } else {
            System.out.println(-1);
        }
    }
}