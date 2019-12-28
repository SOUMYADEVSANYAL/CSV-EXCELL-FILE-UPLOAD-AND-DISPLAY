//package com.java_python.project;
//args: FilePath TableName
import java.io.BufferedReader;
import java.io.InputStreamReader;
//import java.util.Scanner;

public class InsertCSV {

//	private static Scanner sc;

	public static void main(String[] args) {
//		String file_name;
//		String table_name=args[1];
//		sc = new Scanner(System.in);
//		System.out.println("Enter the name of csv file with full path:");
//		file_name = sc.nextLine();
//		System.out.println("Enter the name of the table you want to update:");
//		table_name = sc.nextLine();
		String py_exec[] = {"python","C:/xampp/htdocs/PHP-Java-Python/InsertCSVpy.py",args[0],args[1]};
		try {
			Process p = Runtime.getRuntime().exec(py_exec);
			BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
			String line=null;
			while((line = in.readLine()) != null) {
				System.out.println(line);
			}
			String py_exec_new[] = {"python","C:/xampp/htdocs/PHP-Java-Python/RemoveDuplicatespy.py",args[0]};
			Runtime.getRuntime().exec(py_exec_new);
			String tablename[] = {args[0]};
			RemoveError.main(tablename);
			RemoveDuplicates.main(tablename);
			// EmailVerify.main(tablename);
		} catch (Exception e) {
			e.printStackTrace();
		}
//		System.out.println("CSV File uploaded in "+args[0]+" table");
	}

}
