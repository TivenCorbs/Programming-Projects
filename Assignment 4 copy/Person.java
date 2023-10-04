public class Person {

	private String name;
	private String address;
	private String phone;
	
	
	
	Person(String newName, String address, String phone) {
		
		this.name = newName;
		this.address = address;
		this.phone = phone;
	}
	
	void setName(String name) {//sets the value of the name variable to whatever is type into it by the user
		
		this.name = name;
		//this keyword refers to current object in a method or constructor and most common use of the keyboard is to avoid confusion between class attributes and parameters of the same name	
		
	}
	
	String getName() {//returns what is currently stored in the name variable as a string object
		
		
		return(this.name);
		
	}
	void setPhone(String phone) {
		
		this.phone = phone;
		
		
	}
	
	String getPhone() {
		
		return(this.phone);
		
		
	}
	
	public String toString() {//returns string representation of the object
		return "\nName: " + name +"\nAddress: "+address+ "\nPhone: " + phone;
		
		
	}

	
	

}

    
