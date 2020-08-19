    // Project Goals: Context: You’re part of a research team that has found a new mysterious organism at the bottom of the ocean near hydrothermal vents. Your team names the organism, Pila aequor (P. aequor), and finds that it is only comprised of 15 DNA bases. The small DNA samples and frequency at which it mutates due to the hydrothermal vents make P. aequor an interesting specimen to study. However, P. aequor cannot survive above sea level and locating P. aequor in the deep sea is difficult and expensive. Your job is to create objects that simulate the DNA of P. aequor for your research team to study.

//As you progress through the steps, use the terminal and console.log() statements to check the output of your loops and functions.

// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G'];
    return dnaBases[Math.floor(Math.random() * 4)];
  };
  
// Returns a random single strand of DNA containing 15 bases
const mockUpStrand = () => {
const newStrand = [];
for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
}
return newStrand;
};


//factory function that creates P. aequor objects
const pAequorFactory = (num) => {
    return {
        
        //stores specimen number
        specimenNum: num,
        
        //creates strand of 15 random bases for P aequor
        dna: mockUpStrand(),
        
        //method mutates one of the strands of the P aequor bases, does not allow mutation to be same base
        mutate() {
            const rand_base_idx = Math.floor(Math.random() * this.dna.length);
            const rand_base = this.dna[rand_base_idx];
            do {
                this.dna[rand_base_idx] = returnRandBase();
            }
            while (this.dna[rand_base_idx] === rand_base); 
            return this.dna;
        },

        //method that compares the different base pairs of two different P aequor speciments, and looks at rate of similarity
        compareDNA(pAequor) {
            let iden_bases = 0;
            for (let i = 0; i < this.dna.length; i++) {
                if (this.dna[i] === pAequor.dna[i]) {
                    iden_bases++
                } else{
                    continue
                }
            } const per_same = iden_bases / this.dna.length * 100;
            console.log(`specimen #${this.specimenNum} and specimen #${pAequor.specimenNum} have ${per_same}% DNA in common`)
        },
        
        //method that determines if 60% of the bases are G or C, and returns true if greater than 60%
        willLikelySurvive() {
            let count = 0
            this.dna.forEach(x => {
                if ((x === 'G') || (x === 'C')) {
                    count++
                }
            }); 
            return count / this.dna.length > 0.59;
        },

        //method that creates compliment strand
        complimentStrand() {
            let compliment_strand = []
            this.dna.forEach (x => {
                if (x === 'A') {
                    compliment_strand.push('T');
                }
                else if (x === 'T') {
                    compliment_strand.push('A');
                }
                else if (x === 'G') {
                    compliment_strand.push('C');
                }
                else {
                    compliment_strand.push('G');
                } 
            });
            return compliment_strand;
        }
    }   
}


//storage of 30 different P. aeqor objects
pAequor_store = []
for (let i = 0; i < 30; i++){
    pAequor_store.push(pAequorFactory(i + 1))
}

console.log(pAequor_store)
