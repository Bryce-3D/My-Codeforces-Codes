import java.util.*;

public class Main {

    public static void main(String[] args) {
        // For taking inputs
        Scanner sc = new Scanner(System.in);

        String Homura = sc.nextLine();
        String[] Madoka = Homura.split(" ");
        long n = Integer.parseInt(Madoka[0]);
        long m = Integer.parseInt(Madoka[1]);
        long a = Integer.parseInt(Madoka[2]);

        long x = Math.floorDiv(n-1, a)+1;
        long y = Math.floorDiv(m-1, a)+1;
        long ans = x * y;
        System.out.println(ans);
    }
}
