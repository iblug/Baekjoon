import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 1; i <= n ; i++) {
            bw.write("Hello World, Judge ");
            bw.write(String.valueOf(i));
            bw.write("!\n");
        }

        bw.flush();
        bw.close();
    }
}