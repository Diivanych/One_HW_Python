import java.util.Scanner;

public class Start {
    public static void main(String[] args) {
        System.out.print("\033[H\033[2J");
        Lotto draw = new Lotto();
//        Scanner scan = new Scanner(System.in, "cp866");
        draw.fillToy();
        Scanner scan = new Scanner(System.in, "cp866");
        while (true) {
            System.out.print("""
                Сделайте Ваш выбор:\n
                Просмотреть содержимое базы                      - 1
                Добавить новую игрушку в призовой фонд:          - 2
                Ввести процент выпадения какой-нибудь игрушки:   - 3
                Проведите лотерею и сохраните результаты:        - 4
                ВЫХОД:                                           - 0
                Ваш выбор: ->\s""");
            var selection = scan.next();
            switch (selection) {
                case "1" -> draw.showToy();
                case "2" -> draw.addToy();
                case "3" -> draw.setFrequency();
                case "4" -> draw.Game();
                case "0" -> {
                    System.out.print("\033[H\033[2J");
                    System.out.println("Всего хорошего!\n");
                    System.exit(0);
                }
                default -> {
                    System.out.print("\033[H\033[2J");
                    System.out.println("Неверный ввод. Попробуйте ещё раз.");
                }
            }
        }
    }
}