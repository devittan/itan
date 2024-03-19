public class Message {

    private int idLength;
    private String deviceID;
    private int msgLength;
    private String textMsg;

    public Message(String msg) {
        String[] parts = msg.split(" ");
        if (parts.length != 4) {
            throw new IllegalArgumentException("Invalid message format");
        }

        this.idLength = Integer.parseInt(parts[0]);
        this.deviceID = parts[1];
        this.msgLength = Integer.parseInt(parts[2]);
        this.textMsg = parts[3];
    }

    public boolean isValid() {
        return idLength == deviceID.length() && msgLength == textMsg.length() && textMsg.length() >= 1;
    }

    public int wordCount() {
        int wordCount = 0;
        boolean inWord = false;
        for (char c : textMsg.toCharArray()) {
            if (Character.isWhitespace(c)) {
                inWord = false;
            } else if (!inWord) {
                wordCount++;
                inWord = true;
            }
        }
        return wordCount;
    }
}
