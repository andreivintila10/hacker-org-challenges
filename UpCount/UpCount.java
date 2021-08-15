public class UpCount {

	public long calc(long depth) {
		if (depth == 0) return 1;
		long cc = calc(depth - 1);
		System.out.println(depth + "  " + cc);
		return cc + (depth % 7) + ((((cc ^ depth) % 4) == 0) ? 1 : 0); 
	}

	public long newCalc(long depth) {
		long cc = 1;
		for (long index = 1; index <= depth; index++)
			cc = cc + (index % 7) + ((((cc ^ index) % 4) == 0) ? 1 : 0);
		return cc;
	}

	public static void main(String[] args) {
		UpCount uc = new UpCount();
		long result = uc.newCalc(11589);
		System.out.println(result);
	}
}