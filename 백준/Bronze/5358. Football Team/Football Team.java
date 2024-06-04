import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s;

        while ((s = br.readLine()) != null) {
            s = s.replace('i', '*');
            s = s.replace('I', '_');
            s = s.replace('e', 'i');
            s = s.replace('E', 'I');
            s = s.replace('*', 'e');
            s = s.replace('_', 'E');

            System.out.println(s);
        }
    }
}