import java.util.ArrayList;

public class CarFleet{
    Queue<Car>gasCars;
    Queue<Car>hybridCar;
    Queue<Car>electricCar;
     CarFleet() {
        gasCars = new Queue<Car>();
        hybridCar = new Queue<Car>();
        electricCar = new Queue<Car>();
    }
    public boolean addCar(Car C){
        if(C.getPowerSource()==1){
            gasCars.enqueue(C);
            return true;
        }
        else if(C.getPowerSource()==2){
            hybridCar.enqueue(C);
            return true;
        }
        else if(C.getPowerSource()==3){
            electricCar.enqueue(C);
            return true;
        }
        else{
            return false;
        }
    }
    public ArrayList<Car> processRequests(Queue<Integer>list){
        ArrayList<Car> myList = new ArrayList<Car>();
        int i = 0;
        while(list.isEmpty()==false){
            int data = list.dequeue();
            if(data==1){
                if(gasCars.isEmpty()==false){
                    Car c = gasCars.dequeue();
                    myList.add(c);
                }
                else{
                    Car c = new Car(0,1,0);
                    myList.add(c);
                }
            
            }
            else if(data==2){
                if(hybridCar.isEmpty()==false){
                    Car c = hybridCar.dequeue();
                    myList.add(c);
                }
                else{
                    Car c = new Car(0,2,0);
                    myList.add(c);
                }
            }
            
            else if(data==3){
                if(electricCar.isEmpty()==false){
                    Car c = electricCar.dequeue();
                    myList.add(c);
                }
                else{
                    Car c = new Car(0,3,0);
                    myList.add(c);
                }
            }
            
        }
        return myList;
    }

    
}
