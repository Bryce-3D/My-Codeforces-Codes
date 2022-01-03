import java.util.*;

public class Main {

    public static void main(String[] args) {
        //For taking inputs
        Scanner sc = new Scanner(System.in);

        //Processing the inputs
        String Homura = sc.nextLine();
        String[] Madoka = Homura.split(" ");
        long n = Long.parseLong(Madoka[0]);
        long k = Long.parseLong(Madoka[1]);

        if ( n%2 == 0 ) {
            if ( k <= Math.floorDiv(n,2) ) {
                System.out.println(2*k-1);
            } else {
                System.out.println(2*k-n);
            }
        } else {
            if ( k <= Math.floorDiv(n,2)+1 ) {
                System.out.println(2*k-1);
            } else {
                System.out.println(2*k-n-1);
            }
        }
    }
}
