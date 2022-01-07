import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Looping for each test case
        int nTestCases = Integer.parseInt(sc.nextLine());
        for ( int Kumiko = 0; Kumiko < nTestCases; Kumiko++ ) {
            String[] Homura = sc.nextLine().split(" ");
            int n = Integer.parseInt(Homura[0]);
            int k = Integer.parseInt(Homura[1]);

            if ( n >= 2*k-1 ) { // It's possible
                // Empty row to be used a lot
                String emptyLine = "";
                for ( int i = 0; i < n; i++ ) {
                    emptyLine += ".";
                }

                // Printing out the first row
                String line0 = "R";
                for ( int i = 1; i < n; i++ ) {
                    line0 += ".";
                }
                System.out.println(line0);

                // Printing out the next 2(k-1) rows
                for ( int i = 1; i < k; i++ ) {
                    // Empty line
                    System.out.println(emptyLine);
                    // Row with a rook at the (2i)-th position (0 indexed)
                    String lineI = "";
                    for ( int j = 0; j < 2*i; j++ ) {
                        lineI += ".";
                    }
                    lineI += "R";
                    for ( int j = 0; j < n-2*i-1; j++ ) {
                        lineI += ".";
                    }
                    System.out.println(lineI);
                }

                // Printing the remaining n-(2k-1) empty rows
                for ( int i = 0; i < n-2*k+1; i++ ) {
                    System.out.println(emptyLine);
                }
            } else { // It's not possible
                System.out.println(-1);
            }
        }
    }
}
