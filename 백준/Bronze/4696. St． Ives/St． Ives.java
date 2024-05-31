import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        float n;

        StringBuilder sb = new StringBuilder();

        while ((n = Float.parseFloat(br.readLine())) != 0){
            float a = 1;
            float r = 1;
            for (int i = 0; i < 4; i++) {
                a *= n;
                r += a;
            }
            sb.append(String.format("%.2f", r)).append("\n");
        }

        System.out.println(sb);
    }
}