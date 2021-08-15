package hacker.chal.prot;

import java.awt.Container;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.io.PrintStream;
import javax.swing.JApplet;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;






public class PasswordProtector
  extends JApplet
{
  String dir;
  int width;
  
  public PasswordProtector() {}
  
  private void createGUI()
  {
    width = getSizewidth;
    
    Container cp = getContentPane();
    JPanel panel = new JPanel(new FlowLayout());
    cp.add(panel, "Center");
    
    panel.add(new JLabel("Password:"));
    JTextField pw = new JTextField(12);
    panel.add(pw);
    
    JButton go = new JButton("Check It");
    panel.add(go);
    
    go.addActionListener(new PasswordProtector.1(this, pw));
  }
  
















  public void init()
  {
    try
    {
      SwingUtilities.invokeAndWait(new PasswordProtector.2(this));

    }
    catch (Exception e)
    {

      System.err.println("createGUI didn't successfully complete");
    }
  }
  
  public void start() {}
  
  public void stop() {}
}
