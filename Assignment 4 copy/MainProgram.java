import java.util.Scanner;
public class MainProgram {

    public static void main(String[] args) {
        Scanner k = new Scanner(System.in);
        Persons p = new Persons();
        while(true) {
          System.out.println("\tEnter the options from list below:");
          System.out.println("\t1) Display complete directory");
          System.out.println("\t2) Enter new Person");
          System.out.println("\t3) Search for Person");
          System.out.println("\t4) Modify Person information");
          System.out.println("\t5) Delete a record");
          System.out.println("\t6) Quit");
          System.out.print("Enter your option: ");
          int choice = k.nextInt();
          if(choice == 1) {
            for(int i = 0; i < p.getSize();i++) {
                System.out.println(p.personsList.get(i));
            }
          }
          else if(choice == 2) {
            enterNewPerson(p, k);
          }
          else if(choice == 3) {
            System.out.println("Enter the name of the person you want to search");
            String name = k.next();
            Person f = p.search(name);
            System.out.println(f);
          }
          else if(choice == 4) {
            System.out.println("Enter the name of the person you want to modify");
            String name = k.next();
            Person f = p.search(name);
            System.out.println(f);
            System.out.println("Do you want to modify the information(y/Y)");
            String answer = k.next();
            if(answer.equalsIgnoreCase("y")) {
                System.out.println("Enter the name");
                String name1 = k.next();
                System.out.println("Enter the address");
                k.nextLine();
                String address = k.nextLine();
                System.out.println("\tEnter the phone");
                String phone = k.next();
                Person s = new Person(name,address,phone);
                p.personsList.set(p.personsList.indexOf(f),s);
            }
          }
          else if(choice==5) {
            System.out.println("Enter the index of the record you want to delete");
            int index = k.nextInt();
            if(index >= p.getSize()){
              System.out.println("Error: Invalid index");
            }
            else {
              System.out.println(p.personsList.get(index));
              System.out.println("Do you want to delete this?(y/Y)");
              String answer = k.next();
              if(answer.equalsIgnoreCase("y")){
                p.delete(index);
              }
            }
          }
          else if(choice == 6) {
            break;
          }
          else {
            System.out.println("Invalid Choice: Enter through 1 through 6");
          }
        }
      }
  
    public static void enterNewPerson(Persons p, Scanner k) {
        System.out.println("Enter the name of the Person");
		String name = k.next();//goes to next token
		System.out.println("Enter the address");
    k.nextLine();
		String address = k.nextLine();
		System.out.println("Enter the phone");
		String phone  = k.next();
		System.out.println("Enter the person is a student?(y/Y)");
		String answer = k.next();//next() finds next token from scanner
        if(answer.equalsIgnoreCase("y")){
            System.out.println("Enter the Graduation Year");
            int year = k.nextInt();
            Person s1 = new Student(name, address, phone, year);
            p.add(s1);
        }
        else {
            System.out.println("Enter the person is a employee?(y/Y)");
		    answer = k.next();//next() finds next token from scanner
            if(answer.equalsIgnoreCase("y")){
                System.out.println("Enter the Department");
                String department = k.next();
                Person e1 = new Employee(name, address, phone, department);
                p.add(e1);
            }
            else {
                Person p1 = new Person(name, address, phone);
                p.add(p1);
            }
        }
    }
}
