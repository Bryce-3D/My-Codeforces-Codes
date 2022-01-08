import java.util.*;

public class Main {

    public static void main(String[] args) {
        // For taking inputs
        Scanner sc = new Scanner(System.in);

        // Taking in m and n
        String[] input = sc.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        // Taking in the prices and sorting them
        String[] sPrices = sc.nextLine().split(" ");
        int[] iPrices = new int[sPrices.length];
        for ( int i = 0; i < n; i++ ) {
            iPrices[i] = Integer.parseInt(sPrices[i]);
        }
        Arrays.sort(iPrices);

        /*
        Subtract the negative prices from the total profit until m tvs have
        been bought or until all tvs that give a profit have been bought
         */
        int profit = 0;
        int tracer = 0;
        while ( tracer < m && iPrices[tracer] < 0 ) {
            profit -= iPrices[tracer];
            tracer += 1;
        }

        System.out.println(profit);
    }
}
