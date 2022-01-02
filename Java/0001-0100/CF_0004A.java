import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int w = Integer.parseInt(sc.nextLine());
        if ( w != 2 && w%2 == 0 ) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
