import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        StringBuilder sb = new StringBuilder();
        sb.append(n).append(" is ");
        if ((n & 1) == 1) {
            sb.append("odd");
        } else {
            sb.append("even");
        }
        System.out.print(sb);
    }
}