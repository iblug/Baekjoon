import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        for (int i = a; i <= b; i += 60) {
            bw.write("All positions change in year ");
            bw.write(String.valueOf(i));
            bw.write('\n');
        }

        bw.flush();
        bw.close();
    }
}