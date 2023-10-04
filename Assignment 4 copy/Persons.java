import java.util.ArrayList;
public class Persons {

	ArrayList<Person> personsList;
	public Persons() {
		personsList = new ArrayList<Person>();//initializes a new array as Person
	}
	public Person search(String name) {
		Person p = null;//initialize Person p as null
		for(int i = 0; i <personsList.size();i++) {//travels through Persons list
			if(personsList.get(i).getName().equals(name)){
				if(name.startsWith("s",0)) {

					p = personsList.get(i);

				} 

				
			}
		}
		return p;//returns the p 
	}
	public void add(Person p) {
		personsList.add(p);//adds person to array list
	}
	public int getSize() {
		return personsList.size();//returns list size of persons
	}
	public void delete(int i) {
		if(i<personsList.size()) {
			personsList.remove(i);
		}
	}
	
	public ArrayList<Person> getInternalList() {
		ArrayList<Person>internalList = personsList;//creates new internal lists and assigns Person list
		return internalList;//returns list 
	}
}
    
