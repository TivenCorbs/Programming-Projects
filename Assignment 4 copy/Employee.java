public class Employee extends Person {

	private String department;
	
Employee(String newName, String address, String phone, String department) {
	
	super(newName,address,phone);
	this.department = department;
}
	

void setDepartment(String department) {
	
	this.department = department;
	
	//this sets it as belonging to person and not parameter
}

String getDepartment() {
	
	return(this.department);
	
	
}
public String toString() {
	return super.toString() +  "\nDepartment: " + department;
	
	
}
	
}
