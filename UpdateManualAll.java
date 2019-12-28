//package com.java_python.project;
//args:TableName Roll(old) Email Roll(new) Name
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class UpdateManualAll {

	public static void main(String[] args) {
		String py_exec[] = {"python","C:/xampp/htdocs/PHP-Java-Python/UpdateManualAllpy.py",args[0],args[1],args[2],args[3],args[4]};
		try {
			Process p = Runtime.getRuntime().exec(py_exec);
			BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
			String line=null;
			while((line = in.readLine()) != null) {
				System.out.println(line);
			}
			String py_exec_new[] = {"python","C:/xampp/htdocs/PHP-Java-Python/RemoveDuplicatespy.py",args[1]};
			Runtime.getRuntime().exec(py_exec_new);
			String tablename[] = {args[0]};
			RemoveError.main(tablename);
			RemoveDuplicates.main(tablename);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
