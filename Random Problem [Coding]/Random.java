public class Random {

	public int bucketFromRandom(int randomNumber) {
		int a[]	= new int[10];
		for (int i = 0; i < a.length; i++)
			a[i] = i * randomNumber;
		int index = Math.abs(randomNumber) % a.length;
		return a[index];
	}

	public static void main(String[] args) {
		Random random = new Random();
		for (int index = 0; index < 2147483647; index++)
			System.out.println(index + "  " + random.bucketFromRandom(index));
	}
}