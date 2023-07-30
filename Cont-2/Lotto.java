import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Lotto {

    private static ArrayList<Toy> toys = new ArrayList<>();
    private static ArrayList<Integer> game = new ArrayList<>();
    private static PriorityQueue<String> prizes = new PriorityQueue<>();

    Toy new01 = new Toy(0, "МАЛЬВИНА", 0, 0, 0);
    Toy new02 = new Toy(1, "ПЬЕРО", 0, 0, 0);
    Toy new03 = new Toy(2, "АРТЕМОН", 0, 0, 0);

    private static int idCounter = 4;

    public void fillToy() {
        toys.add(new01);
        toys.add(new02);
        toys.add(new03);
    }

    public void showToy() {
        for(int i = 0; i < toys.size(); i ++)         
            System.out.println("Игрушка № - " +  i + " называется: '" + toys.get(i).getToyTitle() +
            "' имеет процент выпадения " + toys.get(i).getToyVictoryFrequency() + 
            " Нижняя планка " + toys.get(i).getMin() + " Верхняя планка " + toys.get(i).getMax());
    }

    
    public void addToy() {

        int min = 0;
        int max = 0;
        int frequency = 0;
        Scanner scan = new Scanner(System.in, "cp866");
        String title;
        while (true) {
            System.out.print("Введите названиие игрушки: ");
            title = scan.nextLine().toUpperCase();
            if (title.isEmpty()) {
                System.out.println("Неверный ввод. Попробуйте ещё раз.");
                break;
            }
            Toy toy = new Toy(idCounter, title, frequency, min, max);
            if (!toys.contains(toy) || toys.size() == 0) {
                idCounter++;
                toys.add(toy);
                System.out.println("Новая игрушка добавлена.");
            } 
            else {
                System.out.println("Такая игрушка уже есть.");
            }
            break;
        }
    }

    public void setFrequency() {
        Scanner scan = new Scanner(System.in, "cp866");
        String value;

        for(int i = 0; i < toys.size(); i ++) {
            if(i == 0) {
                System.out.println("\nИгрушка " + toys.get(i).getToyTitle() +
                    " имеет процент выпадения " + toys.get(i).getToyVictoryFrequency());
                System.out.print("Введите процент выпадения от 0 до 100:" + " -> ");
                value = scan.nextLine();
            
                if (isDigit(value)) {
                    int newFrequency = Integer.parseInt(value);
                    toys.get(i).setToyVictoryFrequency(newFrequency);
                    toys.get(i).setMin(0);
                    toys.get(i).setMax(toys.get(i).getMin() + newFrequency);

                } else {
                    System.out.println("Неверный ввод. Попробуйте ещё раз.");
                }
            } 
            else {
                
                System.out.println("\nИгрушка " + toys.get(i).getToyTitle() +
                " имеет процент выпадения " + toys.get(i).getToyVictoryFrequency());
                System.out.print("Осталось распределить процент для " + (toys.size() - i) + " игрушек.\n");
                System.out.print("Введите процент выпадения от 0 до:  " + (100 - toys.get(i - 1).getMax()) + " -> ");
                value = scan.nextLine();
            
                if (isDigit(value)) {
                    int newFrequency = Integer.parseInt(value);
                    toys.get(i).setToyVictoryFrequency(newFrequency);
                    toys.get(i).setMin(toys.get(i - 1).getMax());
                    toys.get(i).setMax(toys.get(i).getMin() + newFrequency);
                    
                } else {
                    System.out.println("Неверный ввод. Попробуйте ещё раз.");
                }   
            }
        }
    }

    private static boolean isDigit(String s) throws NumberFormatException {
        try {
            Integer.parseInt(s);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    
    public void Game() {

        game.clear();
        prizes.clear();
        Random rnd = new Random();
        for (int j = 0; j < 10; j ++) {
            int temp = rnd.nextInt(1, 101);
            for( int i = 0; i < toys.size(); i ++) {
                if((temp > toys.get(i).getMin()) & (temp <= toys.get(i).getMax()))
                    game.add(toys.get(i).getToyId());
                    prizes.add(toys.get(i).getToyTitle());
            }
        }
        System.out.println("Печатаем GAME" + game);
        int calc = 0;
        game.toArray();
        for( int i = 0; i < toys.size(); i ++) {
            calc = 0;
            for(int s : game) 
                if(s == i) {
                    calc ++;
                }
            System.out.println("I = " + calc);        

        }
    }

    // public Toy getPrize() {
    //     if (prizes.size() == 0) {
    //         Random rnd = new Random();
    //         for (Toy toy : toys) {
    //             for (int i = 0; i < toy.getToyVictoryFrequency(); i++) {
    //                 Toy temp = new Toy(toy.getToyId(), toy.getToyTitle(), rnd.nextInt(1, 10), toy.getMin(), toy.getMax());
    //                 prizes.add(temp);
    //             }
    //         }
    //     }
    //     return prizes.poll();
    // }

    // public void Lotto() {
    //     if (toys.size() >= 2) {
    //         Toy prize = getPrize();
    //         System.out.println("Приз: " + prize.getToyTitle());
    //         saveResult(prize.getInfo());
    //     } else {
    //         System.out.println("В розыгрыше должно быть более одной игрушки.");
    //     }
    // }

    private void saveResult(String text) {
        File file = new File("Result.txt");
        try {
            file.createNewFile();
        } catch (Exception ignored) {
            throw new RuntimeException();
        }
        try (FileWriter fw = new FileWriter("Result.txt", true)) {
            fw.write(text + "\n");
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
}