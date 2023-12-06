import java.util.Objects;

public class Toy implements Comparable<Toy> {

    private int toyId;
    private String toyTitle;
    private int toyVictoryFrequency;
    private int min;
    private int max;

    public Toy(int toyId, String toyTitle, int toyVictoryFrequency, int min, int max) {
        this.toyId = toyId;
        this.toyTitle = toyTitle;
        this.toyVictoryFrequency = toyVictoryFrequency;
        this.min = min;
        this.max = max;

    }

    public int getToyId() {
        return toyId;
    }

    public String getToyTitle() {
        return toyTitle;
    }

    public int getToyVictoryFrequency() {
        return toyVictoryFrequency;
    }

    public void setToyVictoryFrequency(int toyVictoryFrequency) {
        this.toyVictoryFrequency = toyVictoryFrequency;
    }

    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }


    public String getInfo() {
        return String.format("Номер: %d, Название: %s, Нижняя планка: %d, Вехняя планка: %d", toyId, toyTitle, min, max);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Toy toy = (Toy) o;
        return toyTitle.equals(toy.toyTitle);
    }

    @Override
    public int hashCode() {
        return Objects.hash(toyTitle);
    }

    @Override
    public int compareTo(Toy o) {
        return Integer.compare(this.toyVictoryFrequency, o.toyVictoryFrequency);
    }
}