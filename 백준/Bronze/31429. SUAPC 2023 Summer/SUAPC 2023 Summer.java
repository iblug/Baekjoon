import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static Map<Integer, String> lst;

    public static void main(String[] args) throws IOException {
        lst = new HashMap<>();

        lst.put(1, "12 1600");
        lst.put(2, "11 894");
        lst.put(3, "11 1327");
        lst.put(4, "10 1311");
        lst.put(5, "9 1004");
        lst.put(6, "9 1178");
        lst.put(7, "9 1357");
        lst.put(8, "8 837");
        lst.put(9, "7 1055");
        lst.put(10, "6 556");
        lst.put(11, "6 773");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        System.out.println(lst.get(n));
    }
}