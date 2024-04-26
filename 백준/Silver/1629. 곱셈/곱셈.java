import java.io.IOException;

public class Main {

    public static long c;

    public static void main(String[] args) throws IOException {
        long a = readLong();
        long b = readLong();
        c = readLong();

        System.out.println(pow(a, b));
    }

    public static long pow(long A, long exponent) {
        if(exponent == 1) {
            return A % c;
        }
        long temp = pow(A, exponent / 2);
        if(exponent % 2 == 1) {
            return (temp * temp % c) * A % c;
        }
        return temp * temp % c;

    }

    private static long readLong() throws IOException {
        long v, t = 0;
        while ((v = System.in.read()) > 47) {
            t = t * 10 + (v - 48);
        }
        return t;
    }
}