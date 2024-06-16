import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        int l = readInt();
        int r = readInt() - l;
        if (r > 30) {
            System.out.println("You are speeding and your fine is $500.");
        } else if (r > 20) {
            System.out.println("You are speeding and your fine is $270.");
        } else if (r > 0) {
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