//package com.java_python.project;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class RemoveError {

	public static void main(String[] args) {
		String py_exec[] = {"python","C:/xampp/htdocs/PHP-Java-Python/RemoveErrorpy.py",args[0]};
		try {
			Process p = Runtime.getRuntime().exec(py_exec);
			BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
			String line=null;
			while((line = in.readLine()) != null) {
				System.out.println(line);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
