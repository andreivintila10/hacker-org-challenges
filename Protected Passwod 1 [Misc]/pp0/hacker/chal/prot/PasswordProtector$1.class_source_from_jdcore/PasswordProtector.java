package hacker.chal.prot;

import hacker.chal.prot.PasswordProtector;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

final class PasswordProtector.1
implements ActionListener {
    private final /* synthetic */ JTextField val$pw;

    PasswordProtector.1(JTextField jTextField) {
        this.val$pw = jTextField;
    }

    public void actionPerformed(ActionEvent ev) {
        try {
            String s = Integer.toString(771772773);
            if (s.equals(this.val$pw.getText())) {
                JOptionPane.showMessageDialog(PasswordProtector.this, "correct");
            } else {
                JOptionPane.showMessageDialog(PasswordProtector.this, "wrong");
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}