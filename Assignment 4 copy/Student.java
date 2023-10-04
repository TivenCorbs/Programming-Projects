public class Student extends Person{
	

	private int year;
	
	
	Student(String name, String address, String phone, int year) {
		
		super(name,address,phone);

		this.year = year;
		//this keyword refers to current object in a method or constructor and most common use of the keyboard is to avoid confusion between class attributes and parameters of the same name	
			
		
	}
	
	

void setGraduationYear(int year) {//void indicates method doesn't have return value
	this.year = year;
	
	
}

public int getGraduationYear() {
	
	return year;
}

public String toString() {//returns string representation of the object
	return super.toString() + "\nYear: " + year;	
	
}




}

