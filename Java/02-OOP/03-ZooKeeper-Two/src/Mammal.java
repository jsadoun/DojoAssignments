public class Mammal{
    private int energy = 100;

    public Mammal(){}

    public void setEnergy(int energy){this.energy = energy;}
    public int getEnergy(){return energy;}

    public int displayEnergy(){
        System.out.println("Energy: "+energy);
        return energy;
    }
}
