import java.util.*;

public class Main {
    public static Scanner sc = new Scanner(System.in);
    public static String[] Homura = sc.nextLine().split(" ");
    public static int n = Integer.parseInt(Homura[0]);
    public static int p0 = Integer.parseInt(Homura[1]);
    public static int p1 = Integer.parseInt(Homura[2]);
    public static int p2 = Integer.parseInt(Homura[3]);
    public static int t0 = Integer.parseInt(Homura[4]);
    public static int t1 = Integer.parseInt(Homura[5]);

    /*
    breakPower(t) returns the amount of watts used by Tom's laptop
    when left alone for t minutes after being used
     */
    public static int breakPower(int t) {
        if ( t <= t0 ) { // Still normal mode
            return t * p0;
        } else if ( t <= t0 + t1 ) { // Reached screensaver
            t -= t0;
            return t0 * p0 + t * p1;
        } else { // Reached sleep mode
            t -= t0 + t1;
            return t0 * p0 + t1 * p1 + t * p2;
        }
    }

    public static void main(String[] args) {
        int ans = 0; // The answer

        // First interval to initialize `last_use`
        String[] sInterval = sc.nextLine().split(" ");
        int start = Integer.parseInt(sInterval[0]);
        int end = Integer.parseInt(sInterval[1]);
        ans += (end - start) * p0;
        int lastUse = end;

        // The other n-1 intervals
        for ( int Madoka = 0; Madoka < n-1; Madoka++ ) {
            sInterval = sc.nextLine().split(" ");
            start = Integer.parseInt(sInterval[0]);
            end = Integer.parseInt(sInterval[1]);
            int breakTime = start - lastUse; // How long the laptop wasn't used
            int workTime = end - start;      // How long the laptop was used
            ans += breakPower(breakTime);    // Power used during the break
            ans += workTime * p0;            // Power used during the current session
            lastUse = end;
        }

        System.out.println(ans);
    }
}
