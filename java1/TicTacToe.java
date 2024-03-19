import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class TicTacToe extends JFrame implements ActionListener {

  private final char PLAYER1 = 'X';
  private final char PLAYER2 = 'O';

  private char[][] board = new char[3][3];
  private boolean player1Turn = true;

  private JButton[][] buttons = new JButton[3][3];

  public TicTacToe() {
    super("Tic Tac Toe");
    setLayout(new GridLayout(3, 3));

    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        buttons[i][j] = new JButton();
        buttons[i][j].setFont(new Font("Arial", Font.BOLD, 48));
        buttons[i][j].addActionListener(this);
        add(buttons[i][j]);
      }
    }

    JMenuBar menuBar = new JMenuBar();
    JMenu gameMenu = new JMenu("Game");
    JMenuItem newGameMenuItem = new JMenuItem("New Game");
    newGameMenuItem.addActionListener(this);
    gameMenu.add(newGameMenuItem);
    menuBar.add(gameMenu);
    setJMenuBar(menuBar);

    resetGame();
  }

  @Override
  public void actionPerformed(ActionEvent e) {
    Object source = e.getSource();

    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        if (source == buttons[i][j]) {
          if (board[i][j] == '\u0000') {
            if (player1Turn) {
              board[i][j] = PLAYER1;
              buttons[i][j].setText(String.valueOf(PLAYER1));
              player1Turn = false;
            } else {
              board[i][j] = PLAYER2;
              buttons[i][j].setText(String.valueOf(PLAYER2));
              player1Turn = true;
            }

            if (checkWin(board[i][j], i, j)) {
              JOptionPane.showMessageDialog(this, "Player " + board[i][j] + " wins!");
              resetGame();
            } else if (isBoardFull()) {
              JOptionPane.showMessageDialog(this, "It's a tie!");
              resetGame();
            }
          } else {
            JOptionPane.showMessageDialog(this, "This cell is already occupied!");
          }
          break;
        }
      }
    }

    if (e.getActionCommand().equals("New Game")) {
      resetGame();
    }
  }

  private void resetGame() {
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        board[i][j] = '\u0000';
        buttons[i][j].setText("");
      }
    }
    player1Turn = true;
  }

  private boolean checkWin(char player, int row, int col) {
    // Check row
    for (int i = 0; i < 3; i++) {
      if (board[row][i] != player) {
        break;
      }
    }
    if (i == 3) {
      return true;
    }

    // Check column
    for (int i = 0; i < 3; i++) {
      if (board[i][col] != player) {
        break;
      }
    }
    if (i == 3) {
      return true;
    }

    // Check diagonals
    if (row == col) {
      for (int i = 0; i < 3; i++) {
        if (board[i][i] != player) {
          break;
        }
      }
      if (i == 3) {
        return true;
      }
    }

    if (row + col == 2) {
      for (int i = 0; i < 3; i++) {
        if (board
