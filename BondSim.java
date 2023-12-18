public class BondSim {
    static final double minCostPerVote = 1500.0;
    static final double startPricePerToken = 10.87;
    static final double liquidityPoolInitSize = 90367.0;
    static final double inflation = 1.02;
    double liquidityPoolSize = liquidityPoolInitSize;
    double pricePerToken = startPricePerToken;
    double costIncurred = 0.0;
    
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java BondSim <nVotes>");
            System.exit(1);
        }
        int nVotes = Integer.parseInt(args[0]);
        System.out.println(new BondSim().costOfVotes(nVotes));
    }

    public void buyToken() {
        liquidityPoolSize -= pricePerToken;
        costIncurred += pricePerToken;
        if (liquidityPoolSize < pricePerToken) {
            pricePerToken *= inflation;
            liquidityPoolSize = liquidityPoolInitSize;
        }
    }

    public int tokensPerVote() {
        double numTokens = Math.ceil(minCostPerVote / pricePerToken);
        if (numTokens < 100.0) {
            return 100;
        }
        return (int)Math.round(numTokens);
    }

    public void buyVote() {
        int nTokens = tokensPerVote();
        for (int i = 0; i < nTokens; i++) {
            buyToken();
        }
    }

    public double costOfVotes(int nVotes) {
        for (int i = 0; i < nVotes; i++) {
            buyVote();
// System.out.println("Votes bought: " + (i + 1) + ", total cost: " + costIncurred);
        }
        return costIncurred;
    }
}
