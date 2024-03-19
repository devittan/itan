public class Main {
    public static void main(String[] args) {
        Message msg1 = new Message("08 abc123xy 16 Computer Science");
        boolean msg1Valid = msg1.isValid();
        System.out.println("Message 1 is valid: " + msg1Valid);

        // Create other Message objects and test their validity and word count as needed
    }
}