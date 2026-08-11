Encryption is not about just confidentialiy but also about integrity, authenticiy and non repudiation. for our project goal and strategy we don't need to tack all these four pillars, we will only focus on confidentiality.

---> global goal: updgrade our encryption service to achieve an industry level confidentiality. which include reliability(handle all errors), correctness, performance and security.


---> subgoals:
Add Padding  encryption, we will use RSA-OAEP structure.
        steps:
            - implement or use a library that can generate secure random numbers. (seeds)
             - add a secure hash function, such as SHA-256, to hash the optional OAEP label and to be used internally by MGF1.
            - add mask generation function that take the seeds and length and reture the mask
            - add masked data block constructor function 
            - add message encoder and decoder folowing OAEP template <EM=0x00 ∣∣ maskedSeed ∣∣ maskedDB>
            -
            - switch message transformation to integer from ascii standard to OS2IP (maybe this can be optional) 
                - this include integer --> text and text --> integer
            - encryption part already been settled.
            - add chain of function to unmask the data block : Recover the seed mask --> Recover the original seed --> Recover the data-block mask --> Recover the data block

            - add data block parsers.
            -- add OAEP validation.



Switch to generating large prime numbers, with secure randomness. (size between 2048/3072-bit)
        -  use a secure random number generator library.
        -  add  the validation function, that can validate large size primes,