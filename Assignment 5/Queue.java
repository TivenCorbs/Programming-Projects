import java.util.ArrayList;
public class Queue<e>{
    ArrayList<e>carList;
    public Queue(){
        carList = new ArrayList<e>();

    }
    public void enqueue(e item){
            carList.add(item);
    }
    public e dequeue(){
        e item = null;
        if(carList.size()>0){
            item = carList.get(0);
            carList.remove(0);
        }
        return item;
    }
    public boolean isEmpty(){
        if(carList.size()==0){
            return true;
        }
        else{
            return false;
        }
    }
    public e peek(){
        if(isEmpty()){
            return null;
        }
        e item = carList.get(0);
        return item;
    }
}



    
