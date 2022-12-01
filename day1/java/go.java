import java.io.File;
import java.util.Collections;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.io.FileNotFoundException;


public class go {

    static int returnMostCalorificElf() throws FileNotFoundException {
        // read in file
        File calories = new File("../input.txt");
        Scanner reader = new Scanner(calories);
        // initialise arraylist to hold calorie totals for each elf
        List<Integer> calorie_totals = new ArrayList<Integer>();
        int calorie_count = 0;
        // until we get to the end of the file
        while (reader.hasNextLine()){
            String data = reader.nextLine();
            // if next line is not empty, add the total to the calorie count
            // otherwise, add total to arraylist and reset counter for the next elf
            if (!data.isEmpty()){
                calorie_count += Integer.parseInt(data);
            }
            else {
                calorie_totals.add(calorie_count);
                calorie_count = 0;
            }
        }
        return Collections.max(calorie_totals);
    }


    public static void main(String[] args) throws Exception {
        int total = returnMostCalorificElf();
        System.out.println(total);
    }
}

