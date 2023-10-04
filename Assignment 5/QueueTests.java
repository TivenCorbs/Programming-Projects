import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;

import org.junit.Test;


public class QueueTests{
    Car car1 = new Car(1,1,34.4f);
    Car car2 = new Car(343,2,34.5f);
    Car car3 = new Car(125,3,54.5f);
    Queue<Car> cars = new Queue<Car>();

    @Test
public void testConstructor(){
    assertEquals(true, cars.isEmpty());
  
  
}

@Test
public void testEnqueue(){
    cars.enqueue(car1);
    cars.enqueue(car2);
    cars.enqueue(car3);
   
    assertEquals(false,cars.isEmpty());
    
    
   }
   @Test
public void testDeQueue(){
    assertEquals(null,cars.dequeue());
    
   }

   @Test
   public void testIsEmpty(){
    assertEquals(true, cars.isEmpty());
    
   }

   @Test
public void testPeek(){
    assertEquals(null,cars.peek());

   }
}
