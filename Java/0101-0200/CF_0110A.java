import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String sN = sc.nextLine();
        int nLuckyDigits = 0;

        for ( int i = 0; i < sN.length(); i++ ) {
            if ( sN.charAt(i) == '4' || sN.charAt(i) == '7' ) {
                nLuckyDigits++;
            }
        }

        String sLuckyDigits = Integer.toString(nLuckyDigits);
        boolean almostLucky = true;

        for ( int i = 0; i < sLuckyDigits.length(); i++ ) {
            if ( sLuckyDigits.charAt(i) != '4' && sLuckyDigits.charAt(i) != '7' ) {
                almostLucky = false;
                break;
            }
        }

        if ( almostLucky ) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
