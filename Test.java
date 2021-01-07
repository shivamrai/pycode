//#using two variable swap 2 numbers in java

class Test {
    public static void main(String[] args) {
        int x = 5;
        int y = 10;
        x = x+y;
        y = x-y;
        x = x-y;

        System.out.println("Swap made for x = " +x +" and y= "+y);
    }
}