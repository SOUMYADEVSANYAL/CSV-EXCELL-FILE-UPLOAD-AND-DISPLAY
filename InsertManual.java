//manually insert data in table of database
//package com.java_python.project;
//args: TableName Email Roll Name
//import java.io.BufferedReader;
//import java.io.InputStreamReader;

//table name email rollno name
public class InsertManual {

	public static void main(String[] args) {
//		String table_name = args[0];
//		String name = args[1];
//		String roll = args[2];
		String py_exec[] = {"python","C:/xampp/htdocs/PHP-Java-Python/InsertManualpy.py",args[0],args[1],args[2],args[3]};
		try {
			Runtime.getRuntime().exec(py_exec);
			String py_exec_new[] = {"python","C:/xampp/htdocs/PHP-Java-Python/RemoveDuplicatespy.py",args[1]};
			Runtime.getRuntime().exec(py_exec_new);
			System.out.println("Roll No.: "+args[2]+" Name: "+args[3]+" Email: "+args[1]+" inserted if not present earlier.");
			String tablename[] = {args[0]};
			RemoveError.main(tablename);
			RemoveDuplicates.main(tablename);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
