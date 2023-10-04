public class Car{
    private int id;
    private int powerSource;
    private float PricePerDay;


    Car(int id, int powerSource, float pricePerDay){
        this.id = id;
        this.powerSource = powerSource;
        this.PricePerDay = pricePerDay;
    }

void setId(int id){
    this.id = id;
}
public int getId(){
    return id;
}
void setPowerSource(int PowerSource){
    this.powerSource = PowerSource;
}
public int getPowerSource(){
    return powerSource;
}
public void setPricePerDay(float pricePerDay){
    this.PricePerDay = pricePerDay;
}
public float getPricePerDay(){
    return PricePerDay;
}
}