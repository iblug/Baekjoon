import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int g = Integer.parseInt(br.readLine());

        if (g < 425) {
            System.out.println("Violet");
        } else if (g < 450) {
            System.out.println("Indigo");
        } else if (g < 495) {
            System.out.println("Blue");
        } else if (g < 570) {
            System.out.println("Green");
        } else if (g < 590) {
            System.out.println("Yellow");
        } else if (g < 620) {
            System.out.println("Orange");
        } else {
            System.out.println("Red");
        }
    }
}