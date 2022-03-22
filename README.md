#  Proposed_Solution-Query-refinement_type-aware-approach

**Introduction:**
The goal of this proposed method is to investigate that whether considering query types in query refinement (QR) improve the performance of information retrieval (IR) performance

**Inputs:**

[2009 Million Query track topics (20001-60000)](https://trec.nist.gov/data/million.query09.html)

[query classes](https://trec.nist.gov/data/million.query09.html)

[prels relevance judgments](https://trec.nist.gov/data/million.query09.html)

**Output:**

The out put would be the proper QR method for each qury type.

**Installation:**

**step 1:** Put *2009 Million Query track topics (20001-60000)* and *query classes* files into *dataset* folder. By running *main.py*, the first step of our method, which is to preprocess the input queries, will be applied. The result of this step is *topics.trecMQ* file, which is suitable input for the ReQue(we will explain in the next step).

**step 2:** Install [ReQue](https://github.com/fani-lab/ReQue). Put *topics.trecMQ* and *prels relevance judgments* into *ds*-->*TrecMQ* folder. 

