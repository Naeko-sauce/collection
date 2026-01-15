package com;

public class Master {
    private String name;

    public Master(String name) {
        this.name = name;
    }
    public Master(){

    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    //主人给小哥们喂食
    public void feed(Cat cat,Fish fish){
        System.out.println(cat.getName());
        System.out.println(this.getName()+"给"+cat.getName()+"喂食"+fish.getName());
    }
}
