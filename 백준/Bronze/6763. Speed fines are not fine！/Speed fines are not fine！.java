import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int l = readInt();
        int s = readInt();
        if (s - l > 30) {
            System.out.println("You are speeding and your fine is $500.");
        } else if (s - l > 20) {
            System.out.println("You are speeding and your fine is $270.");
        } else if (s - l > 0) {
            System.out.println("You are speeding and your fine is $100.");
        } else {
            System.out.println("Congratulations, you are within the speed limit!");
        }
    }

    static int readInt() throws IOException {
        int v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}