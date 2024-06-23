import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a = Integer.parseInt(br.readLine());

        bw.write("The largest square has side length ");
        bw.write(String.valueOf((int)Math.sqrt(a)));
        bw.write('.');

        bw.flush();
        bw.close();
    }
}