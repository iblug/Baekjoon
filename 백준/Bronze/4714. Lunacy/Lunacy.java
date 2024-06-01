import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        float n;

        StringBuilder sb = new StringBuilder();

        while ((n = Float.parseFloat(br.readLine())) > 0){
            sb.append(String.format("Objects weighing %.2f on Earth will weigh %.2f on the moon.\n", n, n*0.167));
        }

        System.out.println(sb);
    }
}