import java.util.HashSet;
import java.util.Set;

public class firstDuplicate {

    public int main (int[] a) {
        Set<Integer> seen = new HashSet<Integer>();
        for (int i: a) {
            if (seen.contains(i)) {
                return i;
            }
            seen.add(i);
        }
        return -1;
    }
}
