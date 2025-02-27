// class sieveoferosthesene{
//     public static void main(String [] args){
//         System.out.println("Program to implement Sieve of erosthesene algorithm ");
//         System.out.println("\nThe Sieve of Eratosthenes is an efficient algorithm used to find all prime numbers up to a given number N. It is much faster than checking each number individually for primality.");
//         System.out.println("\nUseful for Large Numbers → Ideal for problems where we need to find multiple prime numbers at once (e.g., competitive programming, cryptography, number theory)."); 
        
//     }
// }

// Java program to print all primes smaller than or equal to
// n using Sieve of Eratosthenes

class sieveoferatosthenes{
	void sieveOfEratosthenes(int n)
	{
		// Create a boolean array "prime[0..n]" and
		// initialize all entries it as true. A value in
		// prime[i] will finally be false if i is Not a
		// prime, else true.
		boolean prime[] = new boolean[n + 1];
		for (int i = 0; i <= n; i++)
			prime[i] = true;

		for (int p = 2; p * p <= n; p++) {
			// If prime[p] is not changed, then it is a
			// prime
			if (prime[p] == true) {
				// Update all multiples of p greater than or
				// equal to the square of it numbers which
				// are multiple of p and are less than p^2
				// are already been marked.
				for (int i = p * p; i <= n; i += p)
					prime[i] = false;
			}
		}

		// Print all prime numbers
		for (int i = 2; i <= n; i++) {
			if (prime[i] == true)
				System.out.print(i + " ");
		}
	}

	// Driver Code
	public static void main(String args[])
	{
		int n = 30080;
		System.out.print("Following are the prime numbers ");
		System.out.println("smaller than or equal to " + n);
		sieveoferatosthenes g = new sieveoferatosthenes();
		g.sieveOfEratosthenes(n);

	}
}