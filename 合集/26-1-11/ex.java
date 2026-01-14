public class ex {
   public static void main(String[] args) {
       Person s  = new Person();
        s.name=("张三");
        s.setAge(2011);
        s.setSalary("5000");
       s.showInfo();
    }
}
class Person{
    public String name;
    private int age;
    private String salary;
    public void setAge(int age){
        if(age >18 && age <60){
            this.age=age;
    }else{
            System.out.println("输入错误");
            this.age = -1;
        }
}
    public int getAge(int age){
        return age;
    }
    public void setSalary(String salary){
        this.salary=salary;
    }
    public String getSalary(String salary){
        return salary;
    }
    public void showInfo(){
        System.out.println("name:"+name+",age:"+age+",salary:"+salary);
    }
}