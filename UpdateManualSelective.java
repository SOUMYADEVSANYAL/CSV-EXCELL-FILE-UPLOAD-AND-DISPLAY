//package com.java_python.project;
//args: TableName Choice(Name,Roll,Email) Roll new_value(Nname||Roll||Email)
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class UpdateManualSelective {

	public static void main(String[] args) {
		if(args[1].equals("Roll")) {
			args[1]="Roll_Number";
		}
		String py_exec[] = {"python","C:/xampp/htdocs/PHP-Java-Python/UpdateManualSelectivepy.py",args[0],args[1],args[2],args[3]};
		try {
			Process p = Runtime.getRuntime().exec(py_exec);
			BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
			String line=null;
			while((line = in.readLine()) != null) {
				System.out.println(line);
			}
			String tablename[] = {args[0]};
			String py_exec_new[] = {"python","C:/xampp/htdocs/PHP-Java-Python/RemoveDuplicatespy.py",args[1]};
			Runtime.getRuntime().exec(py_exec_new);
			if(args[1].equals("Email")) {
				EmailVerify.main(tablename);
			}
			RemoveError.main(tablename);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
