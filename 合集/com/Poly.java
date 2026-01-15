package com;
public class Poly {
    public static void main(String[] args) {
        Master tom  = new Master("汤姆");
        Cat cat2 = new Cat();
        
        Cat cat = new Cat("猫咪");
        tom.feed(cat,new Fish("鱼"));
        
    }
}