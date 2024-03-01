import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int c = System.in.read();
        if (Character.toLowerCase(c) == 'n') {
            System.out.println("Naver D2");
        } else {
            System.out.print("Naver Whale");
        }
    }
}
